import os
import psutil
import threading
import rclpy
import time


from rclpy.node import Node
from std_msgs.msg import Bool, Float32
from cadt02_interfaces.msg import ArduinoFeedback, SmartDriver, MotorFeedback, CameraFeedback
from movement.rmd_motors import run_speed, stop_motor



class RailBotNode(Node):
    def __init__(self):
        super().__init__('railbot_node')

        self.start = 0
        self.flip = False
        self.delay1 = False
        self.delay2 = False
        self.back_down = True
        self.flip = False
        
        # Subscribers
        self.create_subscription(ArduinoFeedback, 'arduino_feedback', self.arduino_feedback_callback, 10)
        self.create_subscription(MotorFeedback, 'motor_feedback', self.motor_feedback_callback, 10)
        self.lidar_pub = self.create_subscription(Float32, 'lidar_dist',self.get_dis_lidar, 10)
        self.create_subscription(CameraFeedback, 'correct_ball', self.camera_feedback, 10)
        self.create_subscription(Bool, 'rail_start',self.rail_start ,10)
        
        # Publisher
        self.smart_driver_pub = self.create_publisher(SmartDriver, '/publish_motor', 10)
        self.timer = self.create_timer(0.1, self.rail_control)

        self.get_dis_lidar = Float32()
        self.limit_sw = ArduinoFeedback()
        self.motor_feed = MotorFeedback()
        self.correct_ball = CameraFeedback()
        self.rail_start = Bool()

        self.ball_verify = False


        self.smart_driver_send(7, 0.0)
        self.sm_control = True
    
    def rail_start(self, msg):
        """
        The function `rail_start` sets to activate the rail.
        
        :param msg: The `rail_start` method seems to be setting the `rail_start` attribute of the object
        to the value of the `msg` parameter. The `msg` parameter is the message or value that will be
        assigned to the `rail_start` attribute
        """
        self.rail_start = msg

    def camera_feedback(self, msg):
        """
        The function `camera_feedback` sets the correct ball based on the input message and verifies it
        against a bottom rail limit switch.
        
        :param msg: The `camera_feedback` method is designed to receive a message (`msg`) and
        update some attributes of the object based on that message. The `msg` parameter likely contains
        information related to a ball detected by a camera
        """
        self.correct_ball = msg
        if self.limit_sw.rail_btm == True:
            self.ball_verify = self.correct_ball.corr_ball

    def get_dis_lidar(self, msg):
        """
        The function `get_dis_lidar` get the distance from the lidar sensor.
        
        """
        self.get_dis_lidar = msg
        
    def motor_feedback_callback(self, msg):
        """
        The function `motor_feedback_callback` get the feedback from the motor.
        
        """
        self.motor_feed = msg

    def arduino_feedback_callback(self, msg):
        """
        The function `arduino_feedback_callback` assigns the value of the `msg` parameter to the `limit_sw`
        attribute of the class instance.
        """
        self.limit_sw = msg
        


    def rail_control(self):
        """
        The rail_control function controls the movement of a motorized rail based on various sensor inputs
        and conditions.
        """
        if self.rail_start.data == True:
            self.get_logger().info(f'Position:{self.motor_feed.position}')
            # # self.get_logger().info(f'Published velocity command: ')
            if self.limit_sw.rail_top == True or self.back_down == True:
                self.back_down = False
                if self.limit_sw.rail_btm == False:
                    self.get_logger().info(f'self.limit_sw.rail_btm{self.limit_sw.rail_btm}')
                    if self.motor_feed.position > -1.0:
                        run_speed(5, -2000)
                    self.rail_down()
                else:
                    stop_motor(5)
                    if self.limit_sw.grp_ball == True:
                        self.smart_driver_send(7, 0.0)

                if self.limit_sw.grp_ball == False:
                    if self.ball_verify == True:
                        self.smart_driver_send(7, 1.0)
                        if not self.delay1:
                            self.get_logger().info('and pg delay 3')
                            time.sleep(1.0)
                            self.delay1 = True
                            self.flip = False
                        run_speed(5, 2000)
                        if not self.flip:
                            self.get_logger().info('initial flip 4')
                            
                            self.smart_driver_send(6, -1.5)
                            self.flip = True
                            self.sm_control = True
                elif self.limit_sw.grp_ball == True:
                    if self.limit_sw.rail_btm == False:
                        if self.motor_feed.position > -1.0:
                            run_speed(5, -2000)
                        self.rail_down()
                        self.delay1 = False
                    else:
                        stop_motor(5)
                        self.rail_down()
            if self.limit_sw.rail_top == False and self.limit_sw.grp_ball == False:
                stop_motor(5)

                if self.flip:
                    self.get_logger().info(f'sm fliipingh')
                    self.smart_driver_send(6, -9.5)
                    self.flip = False
                # if self.motor_feed.position < -9.0:
                #     self.smart_driver_send(6, -9.0, True)
                if self.limit_sw.front_right or self.limit_sw.front_left:
                    if self.limit_sw.grp_ball == False:
                        self.smart_driver_send(7, 0.0)
                        if not self.delay2:
                            time.sleep(0.5)
                            self.delay2 = True
            elif self.limit_sw.rail_top == False and self.limit_sw.grp_ball == True and self.flip == False:
                if not self.sm_control:
                    self.smart_driver_send(6, 0.0)
                    self.sm_control = True
                    self.flip = True 
            else:
                self.back_down = True   
                self.sm_control = True

    def rail_down(self):
        """
        The `rail_down` function checks the status of limit switches and sends commands to a smart driver
        based on certain conditions.
        """
        # self.get_logger().info(f'self.limit_sw.rail_btm{self.limit_sw.rail_btm}')
        if self.limit_sw.grp_ball == True:
            self.smart_driver_send(7, 0.0)
        
        if self.sm_control:
            
            self.get_logger().info(f'sm and sel')
            self.smart_driver_send(6, 0.0)
            # self.smart_driver_send(6, 0.0, True)
            self.sm_control = False

    def smart_driver_send(self, mid, goal, stop=False):
        """
        The `smart_driver_send` function publishes a velocity command message for a smart driver with
        specified parameters.
        
        :param mid: the motor ID
        :param goal: the target angle
        :param stop: The `stop` parameter in the `smart_driver_send` function is a boolean parameter that
        indicates whether the smart driver should stop or not. If `stop` is set to `True`, it means the
        smart driver should stop, and if it is set to `False`, the smart driver should not, defaults to
        False (optional)
        """
        
        msg = SmartDriver()
        msg.speedmode = False
        msg.stop = stop
        msg.motor_id = mid
        msg.goal = goal
        msg.reset = False
        msg.voltagemode = False

        self.smart_driver_pub.publish(msg)
        self.get_logger().info(f'Published velocity command: goal={goal}')

def main(args=None):
    rclpy.init(args=args)
    node = RailBotNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

