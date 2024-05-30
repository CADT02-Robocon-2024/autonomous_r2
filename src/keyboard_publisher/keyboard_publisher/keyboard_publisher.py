import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_publisher')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('KeyboardPublisher has been started.')

    def timer_callback(self):
        try:
            vx = float(input("Enter DistanceX: "))
            vy = float(input("Enter DistanceY: "))
            omega = float(input("Enter omega: "))
        except ValueError:
            self.get_logger().error("Invalid input. Please enter numeric values.")
            return

        msg = Twist()
        msg.linear.x = vx
        msg.linear.y = vy
        msg.angular.z = omega

        self.publisher.publish(msg)
        self.get_logger().info(f'Published velocity command: linear.x={vx}, linear.y={vy}, angular.z={omega}')

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
