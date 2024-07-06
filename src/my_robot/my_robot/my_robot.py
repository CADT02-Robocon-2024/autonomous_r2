import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3  # Import the Vector3 message type
import serial
import struct  # Add this line to import the struct module

# Define your pos object or module here
class Pos:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.h = 0.0

pos = Pos()

class OdometryPublisher(Node):
    def __init__(self):
        super().__init__('odometry_publisher')
        self.publisher = self.create_publisher(Vector3, 'odometry', 10)  # Create a publisher for the 'odometry' topic
        self.ser = serial.Serial('/dev/arduino', 115200)  # Replace '/dev/ttyUSB0' with your serial port and 115200 with your baud rate
        self.get_logger().info('Serial port opened')
        self.create_timer(1.0, self.publish_odometry)  # Publish odometry every 1 second

    # def publish_odometry(self):
    #     try:
    #         while True:  # Continuous reading
    #             if self.ser.read() == b'\xAA':  # Start byte
    #                 odom_data = []
    #                 for _ in range(3):  # Read 3 integers
    #                     low_byte = self.ser.read()
    #                     high_byte = self.ser.read()
    #                     if low_byte is None or high_byte is None:
    #                         break
    #                     # Combine low and high bytes into a signed integer value
    #                     value_bytes = low_byte + high_byte
    #                     value = int.from_bytes(value_bytes, byteorder='little', signed=True)
    #                     odom_data.append(value)
    #                 if self.ser.read() == b'\x55':  # End byte
    #                     msg = Vector3()
    #                     msg.x = float(odom_data[0])
    #                     msg.y = float(odom_data[1])
    #                     msg.z = float(odom_data[2])  # Using z to represent the heading
    #                     self.publisher.publish(msg)
    #                     self.get_logger().info(f'Publishing: x={msg.x}, y={msg.y}, h={msg.z}')
    #     except Exception as e:
    #         self.get_logger().error(f"Error in publish_odometry: {str(e)}")

    #     # Publish received odometry data

    def publish_odometry(self):
        try:
            while True:  # Continuous reading
                if self.ser.read() == b'\xAA':  # Start byte
                    odom_data = []
                    for _ in range(3):  # Read 3 floats
                        float_bytes = self.ser.read(4)
                        if len(float_bytes) < 4:
                            break
                        # Convert bytes to float
                        value = struct.unpack('<f', float_bytes)[0]
                        odom_data.append(value)
                    if len(odom_data) == 3 and self.ser.read() == b'\x55':  # End byte
                        msg = Vector3()
                        msg.x = round(odom_data[0], 2)
                        msg.y = round(odom_data[1], 2)
                        msg.z = round(odom_data[2], 2)  # Using z to represent the heading
                        self.publisher.publish(msg)
                        self.get_logger().info(f'Publishing: x={msg.x:.2f}, y={msg.y:.2f}, h={msg.z:.2f}')
                        print(f'Publishing: x={msg.x:.2f}, y={msg.y:.2f}, h={msg.z:.2f}')  # Debugging print
        except Exception as e:
            self.get_logger().error(f"Error in publish_odometry: {str(e)}")
            print(f"Error in publish_odometry: {str(e)}")

    # Ensure the serial port is correctly initialized in your Python class


def main(args=None):
    rclpy.init(args=args)
    odometry_publisher = OdometryPublisher()
    rclpy.spin(odometry_publisher)
    odometry_publisher.ser.close()  # Close the serial port when the node is shut down
    rclpy.shutdown()

if __name__ == '__main__':
    main()

# test
# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Vector3  # Import the Vector3 message type
# import serial
# import struct

# # Define your pos object or module here
# class Pos:
#     def __init__(self):
#         self.x = 0.0
#         self.y = 0.0
#         self.h = 0.0

# pos = Pos()

# class OdometryPublisher(Node):
#     def __init__(self):
#         super().__init__('odometry_publisher')
#         self.publisher = self.create_publisher(Vector3, 'odometry', 10)  # Create a publisher for the 'odometry' topic
#         self.ser = serial.Serial('/dev/ttyACM0', 115200)  # Replace '/dev/ttyUSB0' with your serial port and 115200 with your baud rate
#         self.get_logger().info('Serial port opened')
#         self.create_timer(1.0, self.publish_odometry)  # Publish odometry every 1 second

#     def publish_odometry(self):
#         if self.ser.is_open:
#             # Send start byte
#             self.ser.write(bytes([0xAA]))

#             # Send pos.x, pos.y, and pos.h as floats over serial
#             for val in [pos.x, pos.y, pos.h]:
#                 self.ser.write(struct.pack('f', val))

#             # Send end byte
#             self.ser.write(bytes([0x55]))

#             self.get_logger().info('Sent data over serial')
#         else:
#             self.get_logger().error('Serial port is not open')

# def main(args=None):
#     rclpy.init(args=args)
#     odometry_publisher = OdometryPublisher()
#     try:
#         rclpy.spin(odometry_publisher)
#     finally:
#         odometry_publisher.ser.close()  # Close the serial port when the node is shut down
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()