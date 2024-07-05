import rclpy
from rclpy.node import Node
from cadt02_interfaces.msg import ArduinoFeedback
import can
import subprocess
import threading

class LimitSwitches(Node):
    def __init__(self):
        super().__init__('limit_switches_node')
        self.publisher_ = self.create_publisher(ArduinoFeedback, 'arduino_feedback', 10)
        self.setup_can_interface()
        self.bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=1000000)

        # Use a separate thread to handle CAN message reception
        self.can_receive_thread = threading.Thread(target=self.receive_response_limitswitch)
        self.can_receive_thread.daemon = True
        self.can_receive_thread.start()

        self.front_right = 0
        self.rail_btm = 0
        self.grp_ball = 0
        self.front_left = 0
        self.start = 0
        self.rail_top = 0
        self.mode = 0
        self.retry = 0

    def setup_can_interface(self):
        cmd = ["ip", "link", "show", "can0"]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if b"state UP" in result.stdout:
            self.get_logger().info("CAN interface is already up")
        else:
            cmd = ["sudo", "ip", "link", "set", "can0", "up", "type", "can", "bitrate", "1000000"]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result.returncode == 0:
                self.get_logger().info("CAN interface is up")
            else:
                self.get_logger().error("CAN failed to setup")

    def receive_response_limitswitch(self):
        while rclpy.ok():
            data = self.bus.recv()
            if data.arbitration_id == 240:
                self.rail_btm = data.data[0]
                self.front_right = data.data[1]
                self.front_left = data.data[2]
                self.grp_ball = data.data[3]
                self.rail_top = data.data[4]
                self.start = data.data[5]
                self.retry = data.data[6]
                self.mode = data.data[7]
                
                feedback_msg = ArduinoFeedback()
                feedback_msg.front_right = bool(self.front_right)
                feedback_msg.rail_btm = bool(self.rail_btm)
                feedback_msg.grp_ball = bool(self.grp_ball)
                feedback_msg.front_left = bool(self.front_left)
                feedback_msg.start = bool(self.start)
                feedback_msg.rail_top = bool(self.rail_top)
                feedback_msg.mode = bool(self.mode)
                feedback_msg.retry = bool(self.retry)

                self.publisher_.publish(feedback_msg)
                self.get_logger().info('Publishing: "%s"' % feedback_msg)

def main(args=None):
    rclpy.init(args=args)
    limit_switches_node = LimitSwitches()
    rclpy.spin(limit_switches_node)
    limit_switches_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
