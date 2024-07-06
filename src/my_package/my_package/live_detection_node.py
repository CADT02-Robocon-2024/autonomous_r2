import rclpy
from rclpy.node import Node
import cv2
import torch
import numpy as np
from ultralytics import YOLO
import math
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class LiveObjectDetectionNode(Node):

    def __init__(self, team_color):
        super().__init__('live_object_detection_node')
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = YOLO("/home/maker/Downloads/best.pt")
        self.bridge = CvBridge()
        self.twist_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_subscription(Vector3, 'odometry', self.odometry_callback, 10)
        self.create_subscription(Image, '/camera/color/image_raw', self.color_image_callback, 10)
        self.create_subscription(Image, '/camera/depth/image_rect_raw', self.depth_image_callback, 10)
        self.team_color = team_color

        self.color_image = None
        self.depth_image = None
        self.depth_scale = 0.001  # Typical scale factor for depth images
        self.pos = Vector3()
        self.timer = self.create_timer(0.1, self.update)  # Call update at 10Hz

    def odometry_callback(self, msg):
        self.pos = msg

    def color_image_callback(self, msg):
        self.color_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        self.get_logger().info('Received color image')

    def depth_image_callback(self, msg):
        self.depth_image = self.bridge.imgmsg_to_cv2(msg, "16UC1")
        self.get_logger().info('Received depth image')

    def send_twist_command(self, linear_x, linear_y, angular_z):
        twist_msg = Twist()
        twist_msg.linear.x = linear_x + self.pos.x
        twist_msg.linear.y = linear_y + self.pos.y
        twist_msg.angular.z = angular_z
        self.twist_publisher.publish(twist_msg)

    def update(self):
        if self.color_image is None or self.depth_image is None:
            self.get_logger().info('Waiting for images...')
            return

        self.get_logger().info('Processing images...')
        fov = math.radians(86)  # Horizontal field of view in radians

        color_image = self.color_image.copy()
        depth_image = self.depth_image.copy()

        # Debugging: show the shape of the images
        self.get_logger().info(f'Color image shape: {color_image.shape}')
        self.get_logger().info(f'Depth image shape: {depth_image.shape}')

        data = self.model(color_image)
        detections = data[0].boxes.data.cpu().numpy()
        self.get_logger().info(f'Number of detections: {len(detections)}')
        
        # detections = [det for det in detections if det[4] > 0.5]

        annotated_image = color_image.copy()

        center_x_selected = None
        depth_selected = None
        nearest_detection_distance = float('inf')

        team_ball_label = "red" if self.team_color == "red" else "blue"

        for det in detections:
            label = f"{self.model.names[int(det[5])]} {det[4]:.2f}"
            self.get_logger().info(f'Detected: {label}')
            box = det[:4]
            center_x = int((box[0] + box[2]) / 2)
            center_y = int((box[1] + box[3]) / 2)

            # Ensure coordinates are within image bounds
            if 0 <= center_x < depth_image.shape[1] and 0 <= center_y < depth_image.shape[0]:
                depth_value = depth_image[center_y, center_x]
                depth = depth_value * self.depth_scale
                label += f" Depth: {depth:.2f} meters"

                if self.model.names[int(det[5])] == team_ball_label and depth < nearest_detection_distance:
                    nearest_detection_distance = depth
                    center_x_selected = center_x
                    depth_selected = depth

                cv2.circle(annotated_image, (center_x, center_y), 5, (0, 255, 255), -1)
                x1, y1, x2, y2 = box.astype(int)
                cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(annotated_image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        if center_x_selected is not None:
            middle_angle = math.atan((center_x_selected - color_image.shape[1] / 2) / (color_image.shape[1] / 2))
            self.send_twist_command(depth_selected * math.cos(middle_angle), depth_selected * math.sin(middle_angle), middle_angle)
            cv2.line(annotated_image, (center_x_selected, center_y), (color_image.shape[1] // 2, color_image.shape[0] // 2), (255, 0, 0), 2)

        cv2.imshow("Live Object Detection", annotated_image)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            rclpy.shutdown()
            cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    team_color = input("Enter your team color (red/blue): ").strip().lower()
    live_object_detection_node = LiveObjectDetectionNode(team_color)
    try:
        rclpy.spin(live_object_detection_node)
    except KeyboardInterrupt:
        pass
    finally:
        live_object_detection_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
