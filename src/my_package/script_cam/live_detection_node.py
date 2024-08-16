# import rclpy
# from rclpy.node import Node
# import cv2
# import pyrealsense2 as rs
# import torch
# import numpy as np
# from ultralytics import YOLO
# import math
# import supervision as sv
# from geometry_msgs.msg import Twist, Vector3
# from std_msgs.msg import Bool
# from collections import OrderedDict
# from cadt02_interfaces.msg import CameraFeedback

# class LiveObjectDetectionNode(Node):

#     def __init__(self, team_color):
#         super().__init__('live_object_tracking_node')
#         self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#         self.model = YOLO("/home/cadt-02/Downloads/ball_v3.2.pt")
#         self.initialize_camera()
#         self.twist_publisher = self.create_publisher(Twist, 'cmd_ball', 10)  # Create the publisher
#         self.create_subscription(Vector3, 'odometry', self.odometry_callback, 10)
#         self.detection_publisher = self.create_publisher(CameraFeedback, 'correct_ball', 10)  # Create the boolean publisher
#         self.team_color = team_color

#         self.pos = Vector3()
#         self.x_offset = 0.00
#         self.y_offset = 0.00
#         self.z_offset = 0.00

#         self.target_pixel = (310, 470)

#         self.next_object_id = 0
#         self.objects = OrderedDict()
#         self.disappeared = OrderedDict()
#         self.max_disappeared = 50

#     def odometry_callback(self, msg):
#         self.pos = msg
#         self.get_logger().info(f'Publishing: x={self.pos.x:.2f}, y={self.pos.y:.2f}, h={self.pos.x:.2f}')

#     def initialize_camera(self):
#         self.pipeline_2 = rs.pipeline()
#         self.config_2 = rs.config()
#         self.config_2.enable_device('239222301831')
#         self.config_2.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
#         self.config_2.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
#         self.profile = self.pipeline_2.start(self.config_2)
#         self.prev_depth_frame = None

#     def capture_depth_frame(self):
#         frames_2 = self.pipeline_2.wait_for_frames()
#         depth_frame_2 = frames_2.get_depth_frame()
#         return depth_frame_2

#     def register(self, centroid):
#         self.objects[self.next_object_id] = centroid
#         self.disappeared[self.next_object_id] = 0
#         self.next_object_id += 1

#     def deregister(self, object_id):
#         del self.objects[object_id]
#         del self.disappeared[object_id]

#     def update_objects(self, input_centroids):
#         input_centroids = [c for c in input_centroids if len(c) == 2]

#         if len(self.objects) == 0:
#             for i in range(len(input_centroids)):
#                 self.register(input_centroids[i])
#         else:
#             object_ids = list(self.objects.keys())
#             object_centroids = list(self.objects.values())

#             for i in range(len(object_centroids)):
#                 self.objects[object_ids[i]] = input_centroids[i] if i < len(input_centroids) else object_centroids[i]

#             if len(input_centroids) > len(object_centroids):
#                 for i in range(len(object_centroids), len(input_centroids)):
#                     self.register(input_centroids[i])

#             if len(input_centroids) < len(object_centroids):
#                 for i in range(len(input_centroids), len(object_centroids)):
#                     object_id = object_ids[i]
#                     self.disappeared[object_id] += 1
#                     if self.disappeared[object_id] > self.max_disappeared:
#                         self.deregister(object_id)

#     def determine_movement(self, center_x, frame_width):
#         """
#         Determine the direction in which the camera needs to move.
#         """
#         if center_x < frame_width // 3:
#             return "left"
#         elif center_x > 2 * frame_width // 3:
#             return "right"
#         else:
#             return "center"

#     def calculate_angle(self, center_x1, center_x2, frame_width, fov):
#         """
#         Calculate the angle by which the camera needs to rotate.
#         """
#         distance1 = abs(center_x1 - frame_width / 2)
#         distance2 = abs(center_x2 - frame_width / 2)
#         angle = math.atan(distance2 / (frame_width / 2) * math.tan(fov / 2)) - math.atan(distance1 / (frame_width / 2) * math.tan(fov / 2))
#         return angle

#     def calc_dist(self, depth, omega):
#         if depth != 0.0:
#             x = math.cos(omega) * depth
#             y = math.sin(omega) * depth
#             self.send_twist_command((x + self.x_offset), (y + self.y_offset), (omega + self.z_offset))
#         else:
#             self.send_twist_command(0.0, 0.0, 0.0)

#     def calculate_middle_angle(self, center_x, frame_width):
#         distance = center_x - frame_width / 2
#         angle = math.atan(distance / (frame_width / 2))
#         return angle

#     def draw_red_dot(self, image):
#         height, width, _ = image.shape
#         center_x = width // 2
#         center_y = height // 2
#         cv2.circle(image, (center_x, center_y), 5, (0, 0, 255), -1)

#     def draw_line_to_middle(self, image, center_x_obj, center_y_obj):
#         height, width, _ = image.shape
#         center_x_middle = width // 2
#         center_y_middle = height // 2
#         cv2.line(image, (int(center_x_obj), int(center_y_obj)), (center_x_middle, center_y_middle), (255, 0, 0), 2)

#     def get_detection_position(self, x, y, depth_value, camera_intrinsics):
#         X = (x - camera_intrinsics[0][2]) * depth_value / camera_intrinsics[0][0]
#         Y = (y - camera_intrinsics[1][2]) * depth_value / camera_intrinsics[1][1]
#         Z = depth_value
#         return X, Y, Z

#     def draw_grid(self, image, num_rows, num_cols, color, thickness):
#         height, width = image.shape[:2]
#         cell_width = width // num_cols
#         cell_height = height // num_rows

#         for i in range(1, num_rows):
#             cv2.line(image, (0, i * cell_height), (width, i * cell_height), color, thickness)

#         for i in range(1, num_cols):
#             cv2.line(image, (i * cell_width, 0), (i * cell_width, height), color, thickness)

#     def send_twist_command(self, linear_x, linear_y, angular_z):
#         twist_msg = Twist()
#         twist_msg.linear.x = linear_x * 100
#         twist_msg.linear.y = linear_y * 100
#         twist_msg.angular.z = angular_z
#         self.twist_publisher.publish(twist_msg)

#     def update(self):
#         while rclpy.ok():
#             depth_sensor = self.profile.get_device().first_depth_sensor()
#             depth_scale = depth_sensor.get_depth_scale()

#             fov = math.radians(86)  

#             grid_color = (255, 255, 255)
#             grid_thickness = 1
#             num_rows = 3
#             num_cols = 3

#             frames_2 = self.pipeline_2.wait_for_frames()
#             color_frame_2 = frames_2.get_color_frame()
#             depth_frame_2 = frames_2.get_depth_frame()
#             if not color_frame_2 or not depth_frame_2:
#                 continue

#             color_image = np.asanyarray(color_frame_2.get_data())
#             depth_image = np.asanyarray(depth_frame_2.get_data())

#             data = self.model(color_image)
#             detections = sv.Detections.from_ultralytics(data[0])
#             detections = [det for det in detections if det[2] > 0.5]

#             annotated_image = color_image.copy()

#             center_x_selected = None
#             depth_selected = None
#             nearest_detection_distance = float('inf')

#             team_ball_label = "red" if self.team_color == "red" else "blue"

#             input_centroids = []
#             detection_status = CameraFeedback()
#             detection_status.corr_ball = True 

#             for det in detections:
#                 label = f"{self.model.model.names[det[3]]} {det[2]:.2f}"
#                 print("Detected:", label)
#                 box = det[0]
#                 center_x = int((box[0] + box[2]) / 2)
#                 center_y = int((box[1] + box[3]) / 2)
#                 depth_value = depth_image[center_y, center_x]
#                 depth = depth_value * depth_scale
#                 label += f" Depth: {depth:.2f} meters"
#                 print(label)

#                 # Check if the detection at (310, 470) is class purple
#                 if center_x == 310 and center_y == 470:
#                     if self.model.model.names[det[3]] == "purple":
#                         detection_status.corr_ball = False  # Set to False if the detection is class purple

#                 if self.model.model.names[det[3]] == team_ball_label and 0.0 < depth < nearest_detection_distance:
#                     nearest_detection_distance = depth
#                     center_x_selected = center_x
#                     depth_selected = depth
#                 else:
#                     print("No team's objects detected")
#                     self.send_twist_command(0.0, 0.0, 0.0)

#                 cv2.circle(annotated_image, (center_x, center_y), 5, (0, 255, 255), -1)
#                 x1, y1, x2, y2 = box.astype(int)
#                 cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                 cv2.putText(annotated_image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#                 self.draw_red_dot(annotated_image)

#                 input_centroids.append((center_x, center_y))

#             self.update_objects(input_centroids)

#             for object_id, centroid in self.objects.items():
#                 if len(centroid) != 2:
#                     continue
#                 cv2.putText(annotated_image, f"ID {object_id}", (centroid[0] - 10, centroid[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#                 cv2.circle(annotated_image, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

#             if center_x_selected is not None:
#                 middle_angle = self.calculate_middle_angle(center_x_selected, color_image.shape[1])
#                 print(f"Adjust camera to middle by {math.degrees(middle_angle):.2f} degrees")
#                 self.calc_dist(depth_selected, middle_angle)
#                 self.draw_line_to_middle(annotated_image, center_x_selected, center_y)

#             self.draw_grid(annotated_image, num_rows, num_cols, grid_color, grid_thickness)
#             cv2.imshow("Live Object Tracking", annotated_image)

#             self.detection_publisher.publish(detection_status)

#             key = cv2.waitKey(1)
#             if key & 0xFF == ord('q'):
#                 break

#             self.prev_depth_frame = depth_frame_2

#         self.pipeline_2.stop()
#         cv2.destroyAllWindows()

# def main(args=None):
#     rclpy.init(args=args)
#     team_color = input("Enter your team color (red/blue): ").strip().lower()
#     live_object_detection_node = LiveObjectDetectionNode(team_color)
#     try:
#         live_object_detection_node.update()
#     except KeyboardInterrupt:
#         pass
#     finally:
#         live_object_detection_node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()








import rclpy
from rclpy.node import Node
import cv2
import pyrealsense2 as rs
import torch
import numpy as np
from ultralytics import YOLO
import math
import supervision as sv
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Bool
from collections import OrderedDict
from cadt02_interfaces.msg import CameraFeedback

class LiveObjectDetectionNode(Node):

    def __init__(self, team_color):
        super().__init__('live_object_tracking_node')
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = YOLO("/home/cadt-02/Downloads/ball_v3.2.pt")
        self.initialize_camera()
        self.twist_publisher = self.create_publisher(Twist, 'cmd_ball', 10)  # Create the publisher
        self.create_subscription(Vector3, 'odometry', self.odometry_callback, 10)
        self.detection_publisher = self.create_publisher(CameraFeedback, 'correct_ball', 10)  # Create the boolean publisher
        self.team_color = team_color

        self.pos = Vector3()
        self.x_offset = 0.00
        self.y_offset = 0.00
        self.z_offset = 0.00

        self.target_pixel = (470, 320)

        self.next_object_id = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()
        self.max_disappeared = 50

    def odometry_callback(self, msg):
        self.pos = msg
        self.get_logger().info(f'Publishing: x={self.pos.x:.2f}, y={self.pos.y:.2f}, h={self.pos.x:.2f}')

    def initialize_camera(self):
        self.pipeline_2 = rs.pipeline()
        self.config_2 = rs.config()
        # self.config_2.enable_device('239222301831')
        self.config_2.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        self.config_2.enable_stream(rs.stream.depth, 848, 480, rs.format.z16, 30)
        self.profile = self.pipeline_2.start(self.config_2)
        self.prev_depth_frame = None

    def capture_depth_frame(self):
        frames_2 = self.pipeline_2.wait_for_frames()
        depth_frame_2 = frames_2.get_depth_frame()
        return depth_frame_2

    def register(self, centroid):
        self.objects[self.next_object_id] = centroid
        self.disappeared[self.next_object_id] = 0
        self.next_object_id += 1

    def deregister(self, object_id):
        del self.objects[object_id]
        del self.disappeared[object_id]

    def update_objects(self, input_centroids):
        input_centroids = [c for c in input_centroids if len(c) == 2]

        if len(self.objects) == 0:
            for i in range(len(input_centroids)):
                self.register(input_centroids[i])
        else:
            object_ids = list(self.objects.keys())
            object_centroids = list(self.objects.values())

            for i in range(len(object_centroids)):
                self.objects[object_ids[i]] = input_centroids[i] if i < len(input_centroids) else object_centroids[i]

            if len(input_centroids) > len(object_centroids):
                for i in range(len(object_centroids), len(input_centroids)):
                    self.register(input_centroids[i])

            if len(input_centroids) < len(object_centroids):
                for i in range(len(input_centroids), len(object_centroids)):
                    object_id = object_ids[i]
                    self.disappeared[object_id] += 1
                    if self.disappeared[object_id] > self.max_disappeared:
                        self.deregister(object_id)

    def determine_movement(self, center_x, frame_width):
        """
        Determine the direction in which the camera needs to move.
        """
        if center_x < frame_width // 3:
            return "left"
        elif center_x > 2 * frame_width // 3:
            return "right"
        else:
            return "center"

    def calculate_angle(self, center_x1, center_x2, frame_width, fov):
        """
        Calculate the angle by which the camera needs to rotate.
        """
        distance1 = abs(center_x1 - frame_width / 2)
        distance2 = abs(center_x2 - frame_width / 2)
        angle = math.atan(distance2 / (frame_width / 2) * math.tan(fov / 2)) - math.atan(distance1 / (frame_width / 2) * math.tan(fov / 2))
        return angle

    def calc_dist(self, depth, omega):
        if depth != 0.0:
            x = math.cos(omega) * depth
            y = math.sin(omega) * depth
            self.send_twist_command((x + self.x_offset), (y + self.y_offset), (omega + self.z_offset))
        else:
            self.send_twist_command(0.0, 0.0, 0.0)

    def calculate_middle_angle(self, center_x, frame_width):
        distance = center_x - frame_width / 2
        angle = math.atan(distance / (frame_width / 2))
        return angle

    def draw_red_dot(self, image):
        height, width, _ = image.shape
        center_x = width // 2
        center_y = height // 2
        cv2.circle(image, (center_x, center_y), 5, (0, 0, 255), -1)

    def draw_line_to_middle(self, image, center_x_obj, center_y_obj):
        height, width, _ = image.shape
        center_x_middle = width // 2
        center_y_middle = height // 2
        cv2.line(image, (int(center_x_obj), int(center_y_obj)), (center_x_middle, center_y_middle), (255, 0, 0), 2)

    def get_detection_position(self, x, y, depth_value, camera_intrinsics):
        X = (x - camera_intrinsics[0][2]) * depth_value / camera_intrinsics[0][0]
        Y = (y - camera_intrinsics[1][2]) * depth_value / camera_intrinsics[1][1]
        Z = depth_value
        return X, Y, Z

    def draw_grid(self, image, num_rows, num_cols, color, thickness):
        height, width = image.shape[:2]
        cell_width = width // num_cols
        cell_height = height // num_rows

        for i in range(1, num_rows):
            cv2.line(image, (0, i * cell_height), (width, i * cell_height), color, thickness)

        for i in range(1, num_cols):
            cv2.line(image, (i * cell_width, 0), (i * cell_width, height), color, thickness)

    def send_twist_command(self, linear_x, linear_y, angular_z):
        twist_msg = Twist()
        twist_msg.linear.x = linear_x * 100
        twist_msg.linear.y = linear_y * 100
        twist_msg.angular.z = angular_z
        self.twist_publisher.publish(twist_msg)

    def update(self):
        while rclpy.ok():
            depth_sensor = self.profile.get_device().first_depth_sensor()
            depth_scale = depth_sensor.get_depth_scale()

            fov = math.radians(86)  

            grid_color = (255, 255, 255)
            grid_thickness = 1
            num_rows = 3
            num_cols = 3

            frames_2 = self.pipeline_2.wait_for_frames()
            color_frame_2 = frames_2.get_color_frame()
            depth_frame_2 = frames_2.get_depth_frame()
            if not color_frame_2 or not depth_frame_2:
                continue

            color_image = np.asanyarray(color_frame_2.get_data())
            depth_image = np.asanyarray(depth_frame_2.get_data())

            data = self.model(color_image)
            detections = sv.Detections.from_ultralytics(data[0])
            detections = [det for det in detections if det[2] > 0.5]

            annotated_image = color_image.copy()

            center_x_selected = None
            depth_selected = None
            nearest_detection_distance = float('inf')

            team_ball_label = "red" if self.team_color == "red" else "blue"

            input_centroids = []
            detection_status = CameraFeedback()
            # detection_status.corr_ball = True 
            target_x = 302
            target_y = 465
            radius = 10  # Define the radius within which you consider the target coordinates to be inside the centroid
            object_found = False

            for det in detections:
                label = f"{self.model.model.names[det[3]]} {det[2]:.2f}"
                print("Detected:", label)
                box = det[0]
                center_x = int((box[0] + box[2]) / 2)
                center_y = int((box[1] + box[3]) / 2)
                depth_value = depth_image[center_y, center_x]
                depth = depth_value * depth_scale
                label += f" Depth: {depth:.2f} meters"
                print(label)

                # Check if the detection at (310, 470) is class purple
                if center_x == 465 and center_y == 302:
                    print("checking ball")
                    if self.model.model.names[det[3]] == "purple":
                        detection_status.corr_ball = False  # Set to False if the detection is class purple
                        self.detection_publisher.publish(detection_status)
                    else:
                        detection_status.corr_ball = True
                        self.detection_publisher.publish(detection_status)

                if self.model.model.names[det[3]] == team_ball_label and 0.0 < depth < nearest_detection_distance:
                    nearest_detection_distance = depth
                    center_x_selected = center_x
                    depth_selected = depth
                else:
                    print("No team's objects detected")
                    self.send_twist_command(20.0, 0.0, 0.0)

                cv2.circle(annotated_image, (center_x, center_y), 5, (0, 255, 255), -1)
                x1, y1, x2, y2 = box.astype(int)
                cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(annotated_image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                self.draw_red_dot(annotated_image)

                if self.is_point_in_box(target_x, target_y, box.astype(int)):
                    object_found = True
                    print("checking ball")
                    if self.model.model.names[det[3]] == "purple":
                        detection_status.corr_ball = False  # Set to False if the detection is class purple
                        self.detection_publisher.publish(detection_status)
                    else:
                        detection_status.corr_ball = True
                        self.detection_publisher.publish(detection_status)

                input_centroids.append((center_x, center_y))

            self.update_objects(input_centroids)

            for object_id, centroid in self.objects.items():
                if len(centroid) != 2:
                    continue
                cv2.putText(annotated_image, f"ID {object_id}", (centroid[0] - 10, centroid[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.circle(annotated_image, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

            if center_x_selected is not None:
                middle_angle = self.calculate_middle_angle(center_x_selected, color_image.shape[1])
                print(f"Adjust camera to middle by {math.degrees(middle_angle):.2f} degrees")
                self.calc_dist(depth_selected, middle_angle)
                self.draw_line_to_middle(annotated_image, center_x_selected, center_y)

            self.draw_grid(annotated_image, num_rows, num_cols, grid_color, grid_thickness)
            cv2.imshow("Live Object Tracking", annotated_image)

            self.detection_publisher.publish(detection_status)

            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break

            self.prev_depth_frame = depth_frame_2

        self.pipeline_2.stop()
        cv2.destroyAllWindows()

    def is_point_in_box(self, x, y, box):
        x1, y1, x2, y2 = box
        return x1 <= x <= x2 and y1 <= y <= y2

def main(args=None):
    rclpy.init(args=args)
    team_color = input("Enter your team color (red/blue): ").strip().lower()
    live_object_detection_node = LiveObjectDetectionNode(team_color)
    try:
        live_object_detection_node.update()
    except KeyboardInterrupt:
        pass
    finally:
        live_object_detection_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()