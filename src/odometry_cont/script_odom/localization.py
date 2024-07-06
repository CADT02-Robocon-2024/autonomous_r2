import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Vector3
import math
import tf_transformations
import serial
import struct

class OdometryNode(Node):

    def __init__(self):
        super().__init__('odometry_node')
        self.imu_counter = 0
        self.offset_yaw = 0.0
        self.corrected_yaw = 0.0
        self.x_position = 0.0
        self.y_position = 0.0
        self.last_left_encoder = 0.0
        self.last_right_encoder = 0.0
        self.last_aux_encoder = 0.0

        self.cm_per_tick = (5.5 * math.pi) / 2000  # cm per tick
        self.LENGTH = 42  # Length of the robot
        self.B = 22.75  # Some characteristic length of the robot, e.g., wheelbase

        self.serial_port = serial.Serial('/dev/arduino', 115200, timeout=1)

        # Subscribers
        self.create_subscription(Imu, 'imu/data_raw', self.imu_callback, 10)
        self.create_subscription(Vector3, 'odometry', self.odometry_callback, 10)

        # Publisher
        self.odom_publisher = self.create_publisher(Odometry, '/odom', 10)

        # Timer for periodic updates
        self.timer = self.create_timer(0.1, self.update_odometry)  # 10 Hz update rate

    def imu_callback(self, msg):
        self.imu = msg
        if self.imu_counter == 0:
            self.offset_w = self.imu.orientation.w
            self.get_logger().info(f'self.offset_w: {self.offset_w}')
            self.imu_counter = 1

        # Get the current yaw from the IMU
        current_yaw = self.imu.orientation.w

        # Normalize current yaw to be within [-PI, PI]
        current_yaw = (current_yaw + math.pi) % (2 * math.pi) - math.pi

        # Calculate corrected yaw
        self.corrected_yaw = current_yaw - self.offset_w

        # Normalize corrected yaw to be within [-PI, PI]
        if self.corrected_yaw > math.pi:
            self.corrected_yaw -= 2 * math.pi
        elif self.corrected_yaw < -math.pi:
            self.corrected_yaw += 2 * math.pi

    def read_serial_data(self):
        if self.serial_port.in_waiting >= 13:  # 1 start byte + 3 floats (4 bytes each)
            start_byte = self.serial_port.read(1)
            if start_byte == b'\xAA':
                data = self.serial_port.read(12)
                x_encoder, y_encoder, heading = struct.unpack('fff', data)
                return x_encoder, y_encoder
        return None, None

    def odometry_callback(self, msg):
        current_left_encoder = msg.x  # Assuming msg.y is the left encoder
        current_right_encoder = msg.x  # Assuming msg.x is the right encoder
        current_aux_encoder = msg.y  # Assuming msg.z is the auxiliary encoder

        # Calculate the differences in encoder ticks
        dn1 = current_left_encoder - self.last_left_encoder
        dn2 = current_right_encoder - self.last_right_encoder
        dn3 = current_aux_encoder - self.last_aux_encoder

        # Update the last encoder readings
        self.last_left_encoder = current_left_encoder
        self.last_right_encoder = current_right_encoder
        self.last_aux_encoder = current_aux_encoder

        # Calculate dtheta, dx, dy
        dtheta = self.degrees_to_radians(self.calc_omega())
        dx = self.cm_per_tick * ((dn1 + dn2) / 2.0)
        dy = self.cm_per_tick * (dn3 - ((dn1 - dn2) * self.B / self.LENGTH))

        # Update the robot's position
        theta = self.corrected_yaw + dtheta / 2.0
        self.x_position += (dx * math.cos(theta)) - (dy * math.sin(theta))
        self.y_position += (dx * math.sin(theta)) + (dy * math.cos(theta))
        self.corrected_yaw += dtheta
        self.corrected_yaw = self.normalize_angle(self.corrected_yaw)

        # Log the encoder values and computed positions
        self.get_logger().info(f'x_encoder: {current_right_encoder}')
        self.get_logger().info(f'y_encoder: {current_left_encoder}')
        self.get_logger().info(f'delta_x: {dx}, delta_y: {dy}')
        self.get_logger().info(f'x: {self.x_position}, y: {self.y_position}, heading: {self.corrected_yaw}')
        
    def degrees_to_radians(self, degrees):
        return degrees * (math.pi / 180.0)

    def calc_omega(self):
        # Placeholder method for calculating angular velocity (omega)
        # Implement your logic for omega calculation here
        return 0.0  # Return omega in degrees

    def normalize_angle(self, angle):
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi:
            angle += 2.0 * math.pi
        return angle

    def update_odometry(self):
        # Publish the odometry message
        # x_encoder, y_encoder = self.read_serial_data()
        # if x_encoder is not None and y_encoder is not None:
        #     self.get_logger().info(f'x_encoder: {x_encoder}')
        #     self.get_logger().info(f'y_encoder: {y_encoder}')
        #     delta_x = x_encoder - self.last_x_encoder
        #     delta_y = y_encoder - self.last_y_encoder

        #     self.last_x_encoder = x_encoder
        #     self.last_y_encoder = y_encoder

        #     self.x_position += delta_x * math.cos(self.corrected_yaw)
        #     self.y_position += delta_y * math.sin(self.corrected_yaw)

        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = 'odom'
        odom_msg.child_frame_id = 'base_link'

        # Set the position
        odom_msg.pose.pose.position.x = self.x_position
        odom_msg.pose.pose.position.y = self.y_position
        odom_msg.pose.pose.position.z = self.corrected_yaw

        # Set the orientation
        quaternion = tf_transformations.quaternion_from_euler(0, 0, self.corrected_yaw)
        odom_msg.pose.pose.orientation.x = quaternion[0]
        odom_msg.pose.pose.orientation.y = quaternion[1]
        odom_msg.pose.pose.orientation.z = quaternion[2]
        odom_msg.pose.pose.orientation.w = quaternion[3]

        # Publish the message
        self.odom_publisher.publish(odom_msg)


def main(args=None):
    rclpy.init(args=args)
    node = OdometryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
