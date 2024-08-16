import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from cadt02_interfaces.msg import Silo

class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_publisher')
        self.publisher = self.create_publisher(Silo, 'silo_num', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('KeyboardPublisher has been started.')

    def timer_callback(self):
        try:
            silo = int(input("Enter Silo num: "))
        except ValueError:
            self.get_logger().error("Invalid input. Please enter numeric values.")
            return

        msg = Silo()
        msg.silo = silo

        self.publisher.publish(msg)
        self.get_logger().info(f'Published Silo num: silo={msg.silo}')

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
