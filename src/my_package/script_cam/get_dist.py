import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import cv2
import numpy as np
import pyrealsense2 as rs2

class ImageListener(Node):
    def __init__(self):
        super().__init__('image_listener')
        self.pipeline_1 = rs2.pipeline()
        self.config_1 = rs2.config()
        self.config_1.enable_device('f1182454')
        self.config_1.enable_stream(rs2.stream.depth, 640, 480, rs2.format.z16, 30)
        self.config_1.enable_stream(rs2.stream.color, 640, 480, rs2.format.bgr8, 30)
        self.profile = self.pipeline_1.start(self.config_1)
        
        self.intrinsics = None
        self.pix = (320, 240)  # Center pixel for 640x480 image
        self.lidar_pub = self.create_publisher(Float32, 'lidar_dist', 10)

    def get_frames(self):
        frames = self.pipeline_1.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            return None, None
        return depth_frame, color_frame

    def process_frames(self):
        while rclpy.ok():
            depth_frame, color_frame = self.get_frames()
            if depth_frame is None or color_frame is None:
                continue

            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())

            distance = depth_image[self.pix[1], self.pix[0]] * depth_frame.get_units()  # Use depth scale
            line = f'\rDepth at pixel({self.pix[0]:3d}, {self.pix[1]:3d}): {distance:.3f}(m).'

            if self.intrinsics:
                depth = depth_image[self.pix[1], self.pix[0]]
                result = rs2.rs2_deproject_pixel_to_point(self.intrinsics, [self.pix[0], self.pix[1]], depth * depth_frame.get_units())
                line += f'  Coordinate: {result[0]:8.2f} {result[1]:8.2f} {result[2]:8.2f}.'
            
            self.get_logger().info(line)
            self.lidar_pub.publish(Float32(data=distance))

            cv2.circle(color_image, self.pix, 5, (0, 0, 255), -1)
            cv2.imshow('Color Image', color_image)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break

    def get_intrinsics(self):
        while not self.intrinsics and rclpy.ok():
            frames = self.pipeline_1.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            if depth_frame:
                video_profile = depth_frame.profile.as_video_stream_profile()
                self.intrinsics = video_profile.get_intrinsics()

def main():
    try:
        rclpy.init()
    except Exception as e:
        print(f"Failed to initialize rclpy: {e}")
        return

    listener = ImageListener()
    listener.get_intrinsics()
    listener.process_frames()
    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
