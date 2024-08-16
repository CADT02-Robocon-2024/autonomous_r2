import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import pyrealsense2 as rs
import numpy as np
import can

# Define the distances to silos
SILO_DISTANCES = {
    1: 25,
    2: 100,
    3: 175,
    4: 250,
    5: 325
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
            print(f"Failed to start pipeline: {e}")
            self.pipeline1 = None
        
        self.bus = can.interface.Bus(channel='can0', bustype='socketcan')
        self.subscriber = self.create_subscription(
            String,
            'can_topic',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        can_id = int(msg.data)
        if can_id in SILO_DISTANCES:
            self.target_distance = SILO_DISTANCES[can_id]
            self.get_logger().info(f'Set target distance to {self.target_distance} cm for CAN ID {can_id}')
        else:
            self.get_logger().warn(f'Unknown CAN ID: {can_id}')
        
        if self.target_distance is not None:
            self.check_distance()

    def check_distance(self):
        frames = self.pipeline1.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        if not depth_frame:
            return

        depth_image = np.asanyarray(depth_frame.get_data())
        height, width = depth_image.shape
        center_distance = depth_image[height // 2, width // 2] * depth_frame.get_units()

        # Convert meters to centimeters
        center_distance_cm = center_distance * 100

        self.get_logger().info(f'Current distance to object: {center_distance_cm:.2f} cm')

        # Implement movement logic based on the distance
        if abs(center_distance_cm - self.target_distance) < 5:
            self.get_logger().info('Reached the target distance.')
            self.target_distance = None
        else:
            self.move_to_silo(center_distance_cm)

    def move_to_silo(self, current_distance):
        # Implement the logic to move the robot to the specified distance
        if current_distance > self.target_distance:
            self.get_logger().info('Moving closer...')
            # Placeholder for actual movement code to move closer
        else:
            self.get_logger().info('Moving away...')
            # Placeholder for actual movement code to move away

def main(args=None):
    rclpy.init(args=args)
    node = SiloMover()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.pipeline1.stop()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
