# Description: This node is responsible for receiving the limit switch status from the Arduino and publishing it to the ROS 2 network.

import rclpy
from rclpy.node import Node
from cadt02_interfaces.msg import ArduinoFeedback
import can
import subprocess
import threading
import os
import psutil

def set_thread_priority():
    p = psutil.Process(os.getpid())
    try:
        p.nice(-20)  # Unix-based systems highest priority
        print("Priority set successfully")
    except psutil.AccessDenied as e:
        print(f"Failed to set thread priority due to permission error: {e}")
    except Exception as e:
        print(f"Failed to set thread priority: {e}")

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
        
        # set_thread_priority()  # Set the thread priority here

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
        """
        This Python function receives data from a CAN bus, extracts specific values, creates a message with
        boolean attributes, and publishes it.
        """
        while rclpy.ok():
            try:
                data = self.bus.recv(1.0)  # Add a timeout to avoid blocking indefinitely
                if data and data.arbitration_id == 240:
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
            except can.CanError as e:
                self.get_logger().error(f"CAN error: {e}")

def main(args=None):
    rclpy.init(args=args)
    limit_switches_node = LimitSwitches()
    rclpy.spin(limit_switches_node)
    limit_switches_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



