import rclpy
from rclpy.node import Node
import cv2
import torch
from ultralytics import YOLO
import numpy as np
from geometry_msgs.msg import Twist
import pyrealsense2 as rs
#from movement.rmd_motors import send_data_can
from collections import OrderedDict

class LiveObjectTrackingNode(Node):

    def __init__(self, team_color):
        super().__init__('live_object_tracking_node')
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = YOLO("/home/cadt-02/Downloads/model_- 9 july 2024 23_22.pt")
        self.team_color = team_color

        self.twist_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.update)  # Call update at 10Hz

        # Configure depth and color streams
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        # Start streaming
        self.pipeline.start(self.config)

        self.color_image = None
        self.depth_image = None
        self.last_ball = None

        # Ball classes
        self.ball_classes = {
            "B": 1, "BB": 2, "BBB": 3, "BBR": 3, "BR": 2, "BRB": 3, "BRR": 3,
            "R": 1, "RB": 2, "RBB": 3, "RBR": 3, "RR": 2, "RRB": 3, "RRR": 3, "silo": 0
        }

        # Silo classes
        self.silo_classes = {
            "SILO 1": 1,
            "SILO 2": 2,
            "SILO 3": 3,
            "SILO 4": 4,
            "SILO 5": 5
        }

        # Tracking variables
        self.next_object_id = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()
        self.max_disappeared = 50

    def register(self, centroid):
        self.objects[self.next_object_id] = centroid
        self.disappeared[self.next_object_id] = 0
        self.next_object_id += 1

    def deregister(self, object_id):
        del self.objects[object_id]
        del self.disappeared[object_id]

    def update_objects(self, input_centroids):
        input_centroids = [c for c in input_centroids if len(c) == 2]

        # If there are no currently tracked objects, register each new input centroid
        if len(self.objects) == 0:
            for i in range(len(input_centroids)):
                self.register(input_centroids[i])
        else:
            object_ids = list(self.objects.keys())
            object_centroids = list(self.objects.values())

            for i in range(min(len(object_centroids), len(input_centroids))):
                self.objects[object_ids[i]] = input_centroids[i]
                self.disappeared[object_ids[i]] = 0

            # Register new centroids if there are more input centroids than existing objects
            if len(input_centroids) > len(object_centroids):
                for i in range(len(object_centroids), len(input_centroids)):
                    self.register(input_centroids[i])

            # Mark disappeared objects if there are fewer input centroids than existing objects
            if len(input_centroids) < len(object_centroids):
                for i in range(len(input_centroids), len(object_centroids)):
                    object_id = object_ids[i]
                    self.disappeared[object_id] += 1
                    if self.disappeared[object_id] > self.max_disappeared:
                        self.deregister(object_id)

    def send_twist_command(self, target_silo, distance):
        #send_data_can(8, target_silo, distance)
        return

    def calculate_silo_priority(self, silo, ball_count, enemy_ball_count):
        if ball_count >= 3:
            return -1  # Skip this silo if it already has 3 balls

        ball_score = (4 - ball_count)
        if silo == "SILO 3":
            ball_score += 10  # Prioritize the middle silo

        if enemy_ball_count == 1:
            ball_score -= 5

        if enemy_ball_count == 2:
            ball_score += 5

        return ball_score
    def check_winning_condition(self, ball_counts):
        silos_with_two_balls = sum(1 for count in ball_counts.values() if count >= 2)
        return silos_with_two_balls >= 3 and self.last_ball in ['R', 'B']  # Ensure last ball is team color

    def is_enemy_close_to_winning(self, enemy_ball_counts):
        silos_with_two_enemy_balls = sum(1 for count in enemy_ball_counts.values() if count >= 2)
        return silos_with_two_enemy_balls >= 3

    def is_team_close_to_winning(self, ball_counts):
        silos_with_two_team_balls = sum(1 for count in ball_counts.values() if count >= 2)
        return silos_with_two_team_balls >= 3

    def update(self):
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            return

        self.depth_image = np.asanyarray(depth_frame.get_data())
        self.color_image = np.asanyarray(color_frame.get_data())

        data = self.model(self.color_image)
        detections = data[0].boxes.data.cpu().numpy()

        if len(detections) == 0:
            self.send_twist_command(0, 0)
            return

        detections = [det for det in detections if det[4] > 0.5]
        annotated_image = self.color_image.copy()

        detections = sorted(detections, key=lambda x: (x[0] + x[2]) / 2)

        ball_counts = {silo: 0 for silo in self.silo_classes.keys()}
        enemy_ball_counts = {silo: 0 for silo in self.silo_classes.keys()}
        silo_distances = {silo: float('inf') for silo in self.silo_classes.keys()}

        input_centroids = []
        for idx, det in enumerate(detections):
            class_id = int(det[5])
            class_name = self.model.names[class_id]
            ball_count = self.ball_classes.get(class_name, 0)

            if class_name in self.ball_classes:
                box = det[:4]
                x1, y1, x2, y2 = box.astype(int)

                if 0 <= x1 < self.color_image.shape[1] and 0 <= y1 < self.color_image.shape[0] and 0 <= x2 < self.color_image.shape[1] and 0 <= y2 < self.color_image.shape[0]:
                    center_x = int((x1 + x2) / 2)
                    center_y = int((y1 + y2) / 2)

                    input_centroids.append((center_x, center_y))

                    cv2.circle(annotated_image, (center_x, center_y), 5, (0, 255, 255), -1)
                    cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(annotated_image, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                    # Ensure the correct assignment of silo name
                    silo_name = list(self.silo_classes.keys())[idx % 5]
                    if class_name.startswith(self.team_color[0].upper()):  # Our team ball
                        ball_counts[silo_name] += ball_count
                    else:  # Enemy team ball
                        enemy_ball_counts[silo_name] += ball_count

                    if self.depth_image is not None:
                        depth_value = self.depth_image[center_y, center_x] * 0.001  # Convert depth to meters
                        # if 0.2 < depth_value < 5.0:  # Ignore depth values that are too low or too high
                        #     silo_distances[silo_name] = min(silo_distances[silo_name], depth_value)

        self.update_objects(input_centroids)

        for object_id, centroid in self.objects.items():
            if len(centroid) != 2:
                continue
            cv2.putText(annotated_image, f"ID {object_id}", (centroid[0] - 10, centroid[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.circle(annotated_image, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

        self.get_logger().info(f'Ball counts: {ball_counts}')
        self.get_logger().info(f'Enemy ball counts: {enemy_ball_counts}')
        self.get_logger().info(f'Silo distances: {silo_distances}')

        available_silos = [silo for silo in self.silo_classes.keys() if ball_counts[silo] < 3]
        if self.is_enemy_close_to_winning(enemy_ball_counts):
            silos_with_two_enemy_balls = [silo for silo in available_silos if enemy_ball_counts[silo] == 2]
            silos_with_two_enemy_balls = sorted(silos_with_two_enemy_balls, key=lambda x: x != 'SILO 3')
            if silos_with_two_enemy_balls:
                selected_silo = silos_with_two_enemy_balls[0]
            else:
                selected_silo = None
        elif self.is_team_close_to_winning(ball_counts):
            silos_with_two_team_balls = [silo for silo in available_silos if ball_counts[silo] == 2 and enemy_ball_counts[silo] <= 1]
            silos_with_two_team_balls = sorted(silos_with_two_team_balls, key=lambda x: x != 'SILO 3')
            if silos_with_two_team_balls:
                selected_silo = silos_with_two_team_balls[0]
            else:
                selected_silo = None
        else:
            silos_with_two_balls = [silo for silo in available_silos if (ball_counts[silo] == 2 or enemy_ball_counts[silo] == 2)]
            free_silos = [silo for silo in available_silos if enemy_ball_counts[silo] == 0]
            one_enemy_ball_silos = [silo for silo in available_silos if enemy_ball_counts[silo] == 1]
            other_silos = [silo for silo in available_silos]

            silos_with_two_balls = sorted(silos_with_two_balls, key=lambda x: x != 'SILO 3')
            free_silos = sorted(free_silos, key=lambda x: x != 'SILO 3')
            one_enemy_ball_silos = sorted(one_enemy_ball_silos, key=lambda x: x != 'SILO 3')
            other_silos = sorted(other_silos, key=lambda x: x != 'SILO 3')

            if silos_with_two_balls:
                selected_silo = silos_with_two_balls[0]
            elif free_silos:
                selected_silo = free_silos[0]
            elif one_enemy_ball_silos:
                selected_silo = one_enemy_ball_silos[0]
            elif other_silos:
                selected_silo = other_silos[0]
            else:
                selected_silo = None

        if selected_silo:
            distance = silo_distances[selected_silo]
            if distance == float('inf'):
                selected_silo_id = self.silo_classes[selected_silo]
                self.get_logger().info(f'Selected silo: {selected_silo}')
                self.send_twist_command(selected_silo_id, 0)
            else:
                self.get_logger().info(f'Selected silo: {selected_silo}')
                selected_silo_id = self.silo_classes[selected_silo]
                self.send_twist_command(selected_silo_id, distance)
                self.last_ball = self.team_color.upper()
        else:
            self.get_logger().info('No suitable silo found')
            self.send_twist_command(0, 0)

        if self.check_winning_condition(ball_counts):
            self.get_logger().info('Congratulations! You have won the Mùa Vàng! Keep playing!')

        cv2.imshow("Live Object Tracking", annotated_image)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            rclpy.shutdown()
            cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    team_color = input("Enter your team color (red/blue): ").strip().lower()
    live_object_tracking_node = LiveObjectTrackingNode(team_color)
    try:
        rclpy.spin(live_object_tracking_node)
    except KeyboardInterrupt:
        pass
    finally:
        live_object_tracking_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()