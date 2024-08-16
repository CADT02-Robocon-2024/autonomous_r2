import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from cadt02_interfaces.msg import LidarDist
import pyrealsense2 as rs
import numpy as np
import can
import subprocess
import threading
import os
import psutil

# Define the distances to silos
SILO_DISTANCES = {
    1: 25.0,
    2: 100.0,
    3: 175.0,
    4: 250.0,
    5: 325.0
}


class SiloMover(Node):
    def __init__(self):
        super().__init__('silo_mover')
        self.target_distance = None
        try:
            # Create a pipeline for each camera
            self.pipeline1 = rs.pipeline()  # L515

            # Create a config and configure it for each camera
            self.config1 = rs.config()

            self.config1.enable_device('f1182454')  # Replace with your L515 serial number

            self.config1.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
            self.config1.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

            # Start the pipeline for each camera,
            self.pipeline1.start(self.config1)
        except RuntimeError as e:
            self.get_logger().error(f"Failed to start pipeline: {e}")
            self.pipeline1 = None

        self.lidar_pub = self.create_publisher(LidarDist, '/publish_range', 10)

        self.dist = LidarDist()
        self.timer = self.create_timer(0.1, self.pub_distance)
        
        # self.bus = can.interface.Bus(channel='can0', bustype='socketcan')
        # self.subscriber = self.create_subscription(
        #     String,
        #     'can_topic',
        #     self.listener_callback,
        #     10
        # )

    def pub_distance(self):
        if self.pipeline1 is None:
            return
        
        frames = self.pipeline1.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        if not depth_frame:
            return

        depth_image = np.asanyarray(depth_frame.get_data())
        height, width = depth_image.shape
        center_distance = depth_image[240, 300] * depth_frame.get_units()
        center_distance_verify = depth_image[240, 350] * depth_frame.get_units()

        # Convert meters to centimeters
        self.dist.y = center_distance * 100
        self.dist.verify = center_distance_verify * 100

        
        if(self.dist.verify != 0 and self.dist.y != 0):
            self.get_logger().info(f'Current distance to object: {self.dist.y:.2f} cm')
            self.get_logger().info(f'Distance verify: {self.dist.verify:.2f} cm')
            self.lidar_pub.publish(self.dist)

def main(args=None):
    rclpy.init(args=args)
    node = SiloMover()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node.pipeline1:
            node.pipeline1.stop()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
