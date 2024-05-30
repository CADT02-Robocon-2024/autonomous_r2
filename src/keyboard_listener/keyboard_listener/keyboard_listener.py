import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3

class KeyboardListener(Node):
    def __init__(self):
        super().__init__('keyboard_listener')
        self.publisher = self.create_publisher(Vector3, 'velocity_command', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('KeyboardListener has been started.')

    def timer_callback(self):
        try:
            vx = float(input("Enter Vx: "))
            vy = float(input("Enter VY: "))
            omega = float(input("Enter omega: "))
        except ValueError:
            self.get_logger().error("Invalid input. Please enter numeric values.")
            return

        msg = Vector3()
        msg.x = vx
        msg.y = vy
        msg.z = omega

        self.publisher.publish(msg)
        self.get_logger().info(f'Published velocity command:Vx={vx},Vy={vy}, z={omega}')

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
