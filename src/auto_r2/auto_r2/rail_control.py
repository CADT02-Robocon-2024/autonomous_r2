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

        # self.can_receive_thread = threading.Thread(target=self.arduino_feedback_callback)
        # self.can_receive_thread.daemon = True
        # self.can_receive_thread.start()
    
    def rail_start(self, msg):
        self.rail_start = msg

    def camera_feedback(self, msg):
        self.correct_ball = msg
        if self.limit_sw.rail_btm == True:
            self.ball_verify = self.correct_ball.corr_ball

    def get_dis_lidar(self, msg):
        self.get_dis_lidar = msg
        
    def motor_feedback_callback(self, msg):
        self.motor_feed = msg

    def arduino_feedback_callback(self, msg):
        self.limit_sw = msg
        


    def rail_control(self):
        # self.rail_btm = msg.rail_btm
        # self.rail_top = msg.rail_top
        # self.grp_ball = msg.grp_ball
        # self.limit_sw = msg
        # self.start = msg.start
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
                # if -0.10 < self.motor_feed.position < 0.10:
                #     self.smart_driver_send(6, -0.10, True )
                    self.flip = True 
            else:
                self.back_down = True   
                self.sm_control = True
        

            


            

                







    def rail_down(self):
        # self.get_logger().info(f'self.limit_sw.rail_btm{self.limit_sw.rail_btm}')
        if self.limit_sw.grp_ball == True:
            self.smart_driver_send(7, 0.0)
        
        if self.sm_control:
            
            self.get_logger().info(f'sm and sel')
            self.smart_driver_send(6, 0.0)
            # self.smart_driver_send(6, 0.0, True)
            self.sm_control = False

    def smart_driver_send(self, mid, goal, stop=False):
        
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




# import os
# import psutil
# import threading
# import rclpy
# import time


# from rclpy.node import Node
# from std_msgs.msg import Bool, Float32
# from cadt02_interfaces.msg import ArduinoFeedback, SmartDriver, MotorFeedback, CameraFeedback
# from movement.rmd_motors import run_speed, stop_motor
# from std_msgs.msg import Float32



# class RailBotNode(Node):
#     def __init__(self):
#         super().__init__('railbot_node')

#         self.start = 0
#         self.flip = False
#         self.delay1 = False
#         self.delay2 = False
#         self.back = False

#         # Subscribers
#         self.create_subscription(ArduinoFeedback, 'arduino_feedback', self.arduino_feedback_callback, 10)
#         self.create_subscription(MotorFeedback, 'motor_feedback', self.motor_feedback_callback, 10)
#         self.lidar_pub = self.create_subscription(Float32, 'lidar_dist',self.get_dis_lidar, 10)
#         self.create_subscription(CameraFeedback, 'correct_ball', self.camera_feedback, 10)
#         self.create_subscription(Bool, 'rail_start', self.rail_callback, 10)
#         self.sm_control = True
        
        
        
        
#         self.smart_driver_pub = self.create_publisher(SmartDriver, '/publish_motor', 10)

#         self.get_dis_lidar = Float32()
#         self.limit_sw = ArduinoFeedback()
#         self.motor_feed = MotorFeedback()
#         self.rail_bool = Bool()

#         # self.smart_driver_send(7, 0.0)
#     def rail_callback(self, msg):
#         self.rail_bool = msg

#     def get_dis_lidar(self, msg):
#         self.get_dis_lidar = msg
        
#     def motor_feedback_callback(self, msg):
#         self.motor_feed = msg
        
#     def camera_feedback(self, msg):
#         self.correct_ball = msg

#     def arduino_feedback_callback(self, msg):
#         self.limit_sw = msg
#         self.get_logger().info(f'Position:{self.motor_feed.position}')
        # if self.limit_sw.rail_btm == False and self.limit_sw.grp_ball == True:
        #     self.get_logger().info(f'Going down')
        #     self.get_logger().info(f'self.sm_control{self.sm_control}')
        #     self.rail_down()
        # elif self.limit_sw.rail_btm == True:
        #     stop_motor(5)

        # if self.limit_sw.rail_top == True and self.limit_sw.grp_ball == False:
        #     self.get_logger().info(f'Going up')
        #     self.rail_up()
        # elif self.limit_sw.rail_top == False and self.limit_sw.grp_ball == True:
        #     stop_motor(5)
        # if self.start == 0: #move down
        #     if self.limit_sw.rail_btm == False and self.limit_sw.rail_top == True:
        #         self.smart_driver_send(7, 0.0)
        #         self.get_logger().info(f'rail_btm{self.limit_sw.rail_btm}')
                
        #         # run_speed(5, -1000) 
        #         self.smart_driver_send(6, -0.10)
        #     self.start = 1
                
        # elif self.start == 1:
        #     if self.motor_feed.position > -1.0:
        #         run_speed(5, -1000)
        #     self.start = 2
        # elif self.start == 2:
        #     if self.limit_sw.rail_btm == True:
        #         self.smart_driver_send(7, 0.0)
        #         stop_motor(5)
        #         self.get_logger().info(f'rail_btm{self.limit_sw.rail_btm}')
        #         self.smart_driver_send(6, 0.0, True)
        #         self.start = 3
        # elif self.start == 3:
        #     if self.limit_sw.grp_ball == False and self.limit_sw.rail_top == True and self.limit_sw.rail_btm == True:
        #         self.smart_driver_send(7, 1.0)
        #         self.start = 4
                
        #     # else:
        #     #     self.start1 = True
        # elif self.start == 4:
        #     if self.limit_sw.rail_top == True and self.limit_sw.rail_btm == True and self.limit_sw.grp_ball == False:
        #         if not self.delay1:
        #             self.get_logger().info('and pg delay 3')
        #             time.sleep(1.0)
        #             self.delay1 = True
        #         run_speed(5, 1000)
        #         if not self.flip:
        #             self.get_logger().info('initial flip 4')
                    
        #             self.smart_driver_send(6, -0.65)
        #             self.flip = True
        #         self.start = 5
        # elif self.start == 5:
        #     self.flip = False 
        #     if self.limit_sw.rail_top == False:
        #         self.get_logger().info('stop rail 5')
        #         stop_motor(5)
        #         if not self.flip:
        #             # print("initial flip")
        #             self.smart_driver_send(6, -9.5)
        #             self.flip = False
        #         self.start = 6
        #     # if self.limit_sw.grp_ball == True:
        #     #     self.start1 = True
        # elif self.start == 6:
        #     self.delay2 = False
        #     if self.limit_sw.front_right or self.limit_sw.front_left:
        #         if self.limit_sw.grp_ball == False:
        #             self.smart_driver_send(7, 0.0)
                    
        #             if not self.delay2:
        #                 # print("delayyyy release")
        #                 time.sleep(0.5)
        #                 self.delay2 = True
        #             # if self.limit_sw.rail_top == False:
        #             #     self.start6 = False
        #             #     self.start0 = True
        #             self.start = 7
        # elif self.start == 7:
        #     if self.limit_sw.grp_ball == True and self.limit_sw.rail_top == False and self.limit_sw.rail_btm == False:
        #         self.start = 0
       ################################################################### 
        
        # if self.start == 0: #move down
        #     if self.limit_sw.rail_btm == False:
        #         self.smart_driver_send(7, 0.0)
        #         self.get_logger().info(f'rail_btm{self.limit_sw.rail_btm}')
        #         # run_speed(5, -1000) 
        #         self.smart_driver_send(6, -0.10)
        #     self.start = 1
            
        # elif self.start == 1:
        #     if self.motor_feed.position > -1.0:
        #         run_speed(5, -1000)
        #     self.start = 2

        # elif self.start == 2:
        #     if self.limit_sw.rail_btm == True:
        #         self.smart_driver_send(7, 0.0)
        #         stop_motor(5)
        #         self.get_logger().info(f'rail_btm{self.limit_sw.rail_btm}')
        #         self.smart_driver_send(6, 0.0, True)
        #         self.start = 3

        # elif self.start == 3:
        #     if self.limit_sw.grp_ball == False and self.limit_sw.rail_top == True and self.limit_sw.rail_btm == True:
        #         self.smart_driver_send(7, 1.0)
        #         self.start = 4
        #         self.back = True
                
        # elif self.start == 4:
        #     if self.limit_sw.rail_top == True and self.limit_sw.rail_btm == True and self.limit_sw.grp_ball == False and self.correct_ball.corr_ball == True:
        #         if not self.delay1:
        #             self.get_logger().info('and pg delay 3')
        #             time.sleep(1.0)
        #             self.delay1 = True
        #         run_speed(5, 1000)
        #         if not self.flip:
        #             self.get_logger().info('initial flip 4')
        #             self.smart_driver_send(6, -0.65)
        #             self.flip = True
        #         self.start = 5
        #         self.back = True
        #     else:
        #         self.start = 1

        # elif self.start == 5:
        #     self.flip = False 
        #     if self.limit_sw.rail_top == False and self.limit_sw.grp_ball == False:
        #         self.get_logger().info('stop rail 5')
        #         stop_motor(5)
        #         if not self.flip:
        #             self.smart_driver_send(6, -9.5)
        #             self.flip = False
        #         self.start = 6
        #         self.back = True
        # elif self.limit_sw.grp_ball == True:
        #     if self.back == True:
        #         self.start = 0
        #         self.back = False

        # elif self.start == 6:
        #     self.delay2 = False
        #     if self.limit_sw.front_right or self.limit_sw.front_left:
        #         if self.limit_sw.grp_ball == False:
        #             self.smart_driver_send(7, 0.0)
        #             if not self.delay2:
        #                 time.sleep(0.5)
        #                 self.delay2 = True
        #             self.start = 7

        # elif self.start == 7:
        #     if self.limit_sw.rail_btm == False and self.limit_sw.rail_top == False:
        #         self.smart_driver_send(7, 0.0)
        #         self.get_logger().info(f'rail_btm{self.limit_sw.rail_btm}')
        #         # run_speed(5, -1000) 
        #         self.smart_driver_send(6, -0.10)
        #     self.start = 8
            
        # elif self.start == 8:
        #     if self.limit_sw.rail_top == False:
        #         if self.motor_feed.position > -1.0:
        #             run_speed(5, -1000)
        #             self.start = 9

        # elif self.start == 9:
        #     if self.limit_sw.rail_btm == True and self.limit_sw.rail_top == True:
        #         self.smart_driver_send(7, 0.0)
        #         stop_motor(5)
        #         self.get_logger().info(f'rail_btm{self.limit_sw.rail_btm}')
        #         self.smart_driver_send(6, 0.0, True)
        #         self.start = 3
                

#     def rail_down(self):
#             # self.get_logger().info(f'self.limit_sw.rail_btm{self.limit_sw.rail_btm}')
#             run_speed(5, -1000)
            
#             if self.sm_control:
#                 self.smart_driver_send(7, 0.0)
#                 self.get_logger().info(f'sm and sel')
#                 self.smart_driver_send(6, -0.10)
#                 self.smart_driver_send(6, 0.0, True)
#                 self.sm_control = False

#     def rail_up(self):
#             run_speed(5, 1000)
#             if self.sm_control:
#                 self.smart_driver_send(7, 1.0)
#                 self.get_logger().info(f'sm and sel')
#                 self.smart_driver_send(6, -0.10)
#                 self.smart_driver_send(6, 0.0, True)
#                 self.sm_control = False

#     def smart_driver_send(self, mid, goal, stop=False):
        
#         msg = SmartDriver()
#         msg.speedmode = False
#         msg.stop = stop
#         msg.motor_id = mid
#         msg.goal = goal
#         msg.reset = False
#         msg.voltagemode = False

#         self.smart_driver_pub.publish(msg)
#         self.get_logger().info(f'Published velocity command: goal={goal}')

# def main(args=None):
#     rclpy.init(args=args)
#     node = RailBotNode()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()


# if __name__ == '__main__':
#     main()




