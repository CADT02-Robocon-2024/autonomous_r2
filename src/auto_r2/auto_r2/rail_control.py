import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Float32
from cadt02_interfaces.msg import ArduinoFeedback, SmartDriver
from movement.rmd_motors import run_speed

class RailBotNode(Node):
    def __init__(self):
        super().__init__('railbot_node')
        
        self.start = 0
        self.flip = False

        self.create_timer(1.0, self.timer_callback)  # 1 Hz timer

        # Subscribers
        self.arduino_feedback_sub = self.create_subscription(ArduinoFeedback, 'arduino_feedback', self.arduino_feedback_callback, 10)
        self.smart_driver_sub = self.create_subscription(SmartDriver, 'smart_driver_feedback', self.smart_driver_callback, 10)

        # Publishers
        # self.solenoid_pub = self.create_publisher(Bool, '/publish_solenoid', 10)
        self.smart_driver_pub = self.create_publisher(SmartDriver, '/publish_motor', 10)

        # self.arduino_feedback = None
        self.smart_driver = SmartDriver()

    def arduino_feedback_callback(self, msg):
        self.arduino_feedback = msg

    def smart_driver_callback(self, msg):
        self.smart_driver = msg

    def timer_callback(self):
        if not self.arduino_feedback or not self.smart_driver:
            return
        
        print(f"SmartDriver Position: {self.smart_driver.goal}")
        print(f"RailBot: {self.arduino_feedback.rail_btm}")

        if self.start == 0:
            print("case 1")
            if self.arduino_feedback.rail_btm == 0:
                print("running to bottom")
                self.motor_pub.publish(smart)
                self.solenoid_pub.publish(Bool(data=False))
                
                if not self.flip:
                    print("initial flip")
                    self.smart_driver_pub.publish(SmartDriver(motor_id=0, goal=0, speedmode=False, stop=False, reset=False, voltagemode=True))
                    
                    if -0.05 < self.smart_driver.goal < 0.05:
                        print("stop motor")
                        self.smart_driver_pub.publish(SmartDriver(motor_id=0, goal=0, speedmode=False, stop=True, reset=False, voltagemode=True))
                    self.flip = True
            elif self.arduino_feedback.rail_btm == 1:
                print("stop rail")
                self.motor_pub.publish(Float32(data=0))
                self.start = 1
                self.flip = False
        elif self.start == 1:
            print("case 2")
            if self.arduino_feedback.grp_ball == 0:
                self.solenoid_pub.publish(Bool(data=True))
                print("grab ball")
                if self.arduino_feedback.rail_top == 1:
                    print(self.arduino_feedback.rail_top)
                    self.motor_pub.publish(Float32(data=1000))
                    if not self.flip:
                        print("initial flip")
                        self.smart_driver_pub.publish(SmartDriver(motor_id=0, goal=-2, speedmode=False, stop=False, reset=False, voltagemode=True))
                        self.flip = True
                    if self.arduino_feedback.rail_top == 0:
                        self.motor_pub.publish(Float32(data=0))

                else:
                    print("stop rail")
                    self.motor_pub.publish(Float32(data=0))
                    self.smart_driver_pub.publish(SmartDriver(motor_id=0, goal=-3.5, speedmode=False, stop=False, reset=False, voltagemode=True))
                    self.start = 2
            else:
                print("case 3")
                self.start = 0
                self.flip = False

def main(args=None):
    rclpy.init(args=args)
    railbot_node = RailBotNode()
    rclpy.spin(railbot_node)
    railbot_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
