import rclpy
from rclpy.node import Node
from cadt02_interfaces.msg import SmartDriver

class SmartDriverTest(Node):
    def __init__(self):
        super().__init__('keyboard_publisher')
        self.publisher = self.create_publisher(SmartDriver, '/publish_motor', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('SmartDriverTest has been started.')

    def timer_callback(self):
        try:
            # speed_mode = bool(input("Enter speed mode: "))
            # stop = bool(input("Enter stop mode: "))
            mid = int(input("Enter motor id: "))
            goal = float(input("Enter goal: "))
        except ValueError:
            self.get_logger().error("Invalid input. Please enter numeric values.")
            return

        msg = SmartDriver()
        msg.speedmode = False
        msg.stop = False
        msg.motor_id = mid
        msg.goal = goal
        msg.reset = False
        msg.voltagemode = False

        self.publisher.publish(msg)
        self.get_logger().info(f'Published velocity command: goal={goal}')

def main(args=None):
    rclpy.init(args=args)
    node = SmartDriverTest()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
