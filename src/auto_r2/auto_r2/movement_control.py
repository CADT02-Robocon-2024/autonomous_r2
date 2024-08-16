# import rclpy
# import time
# import math

# from rclpy.node import Node
# from geometry_msgs.msg import Twist, Vector3
# from cadt02_interfaces.msg import WayPoint, ArduinoFeedback, CameraFeedback, SmartDriver, Silo
# from get_dist import get_dist
# from std_msgs.msg import Float32, Bool


# SILO_DISTANCES = {
#     1: 28.0,
#     2: 106.0,
#     3: 179.0,
#     4: 254.0,
#     5: 332.0,
#     0: 179.0,
# }


# class WaypointProvider(Node):

#     def __init__(self):
#         super().__init__('waypoint_provider')

#         # Publisher to send waypoints
#         self.waypoint_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

#         # Subscriber to get feedback from MovementControl
#         self.create_subscription(WayPoint, 'wp_done', self.wp_done_callback, 10)
#         self.create_subscription(Vector3, 'odometry', self.odometry_callback, 10)
#         self.create_subscription(ArduinoFeedback, 'arduino_feedback', self.arduino_feedback_callback, 10)
#         self.create_subscription(Twist, 'cmd_ball', self.cmd_ball_callback, 10)
#         self.create_subscription(Silo, 'silo_num', self.silo_callback, 10)
#         self.create_subscription(CameraFeedback, 'correct_ball', self.camera_feedback, 10)

#         self.create_subscription(Vector3, 'oreintation', self.oreintation_callback, 10)
#         self.create_subscription(Float32, 'publish_range', self.lidar_dist, 10)

#         self.smart_driver_pub = self.create_publisher(SmartDriver, '/publish_motor', 10)
#         self.rail_start = self.create_publisher(Bool, 'rail_start', 10)
        

#         self.pos = Vector3()
#         self.limit_sw = ArduinoFeedback()
#         self.silo = Silo()
#         self.lidar = Float32()
#         self.rail_bool = Bool()
#         self.lidar_diff = 0.0

#         # Define waypoints
#         # self.waypoints = []

#         # self.waypoints = [(550.0, 0.0,0.0, 120.0), (580.0, -385.0,0.0, 60.0),(580.0 + 330,-385.0,0.0, 20.0),(580.0 + 330,-385.0,90.0, 0.0),(542.0, -387.0, 90.0, 0.0)]
#         self.waypoint_retry = [(80.0, 0.0,0.0, 20.0), (90.0, -385.0,0.0, 60.0),(90.0 + 330,-385.0,0.0, 20.0),(90.0 + 330,-385.0,90.0, 0.0),(72.0, -387.0, 90.0, 0.0)]
#         # self.waypoint2 = [(self.pos.x + 300.0, self.pos.y, 0.0, 0.0)]
#         # self.waypoints = [(200.0,0.0,0.0, 20.0),(200.0,0.0,90.0, 10.0)]
#         self.waypoints = [(550.0, 0.0,0.0, 120.0), (580.0, 385.0,0.0, 60.0),(580.0 + 330,385.0,0.0, 20.0),(580.0 + 330,385.0,90.0, 0.0)]
#         # self.waypoints = [(0.0, -400.0, 60.0),(330.0,-400.0, 0.0)]
#         # self.waypoints = [(330.0, 0.0, 0.0, 20.0),(330.0, 0.0, 90.0, 0.0),(self.pos.x - 380.0, self.pos.y, 90.0, 0.0)]
#         self.current_waypoint_index = 0
#         self.waypoint = Twist()
#         self.orientation = Vector3()
#         self.correct_ball = CameraFeedback()

#         # Publish the first waypoint
#         # self.publish_next_waypoint()

#         self.position = None
#         self.begin = 0

#         self.target_b_x = 0.0
#         self.target_b_y = 0.0
#         self.target_b_z = 0.0


#         self.change_imu = 0.0
#         self.settled_turn = False


#         self.yellow_home = True
#         self.ball_verify = False

    
#     def camera_feedback(self, msg):
#         self.correct_ball = msg
#         if self.limit_sw.rail_btm == True:
#             self.ball_verify = self.correct_ball.corr_ball
#     def lidar_dist(self, msg):
#         self.lidar = msg

#     def silo_callback(self, msg):
#         self.silo = msg
#         if self.silo.silo != 0:
#             self.yellow_home = False
#         else :
#             self.yellow_home = True

#     def oreintation_callback(self, msg):
#         self.orientation = msg
    

#     def cmd_ball_callback(self, msg):
#         self.target_b_x = msg.linear.x
#         self.target_b_y = msg.linear.y
#         theta = math.atan2(self.target_b_y, self.target_b_x)
#         self.target_b_z = theta
        

#     def arduino_feedback_callback(self, msg):
#         # self.rail_btm = msg.rail_btm
#         # self.rail_top = msg.rail_top
#         # self.grp_ball = msg.grp_ball
#         # self.start = msg.start

#         self.limit_sw = msg
#         if self.limit_sw.grp_ball == True and self.limit_sw.front_right == True:
#             self.yellow_home = True
#         else: 
#             self.yellow_home = False
        

#         if self.limit_sw.start:
#             self.begin = 1
#         if self.limit_sw.retry:
#             self.begin = 2
#         if self.limit_sw.mode:
#             self.begin = 4


#     def odometry_callback(self, msg):
#         self.pos = msg
#         # self.waypoints = [(550.0, 0.0,0.0, 120.0), (580.0, -385.0,0.0, 60.0),(580.0 + 330,-385.0,0.0, 20.0),(580.0 + 330,-385.0,90.0, 0.0),(542.0, -387.0, 90.0, 0.0)]
#         self.waypoint_retry = [(80.0, 0.0,0.0, 20.0), (90.0, -385.0,0.0, 60.0),(90.0 + 330,-385.0,0.0, 20.0),(90.0 + 330,-385.0,90.0, 0.0),(72.0, -387.0, 90.0, 0.0)]
#         # self.waypoint2 = [(self.pos.x + 300.0, self.pos.y, 0.0, 0.0 )]
#         self.waypoints = [(200.0,0.0,0.0, 20.0),(200.0,0.0,90.0, 0.0)]
#         # self.waypoints = [(330.0, 0.0, 0.0, 20.0),(330.0, 0.0, 90.0, 0.0),(self.pos.x - 380.0, self.pos.y, 90.0, 0.0)]
        

#     def publish_next_waypoint(self):
#         # self.get_logger().info(f'Publishing error {self.waypoints[self.current_waypoint_index][0]}')
#         if self.current_waypoint_index < len(self.waypoints):
#             if self.current_waypoint_index == 1:
#                 self.rail_bool.data = True
#                 self.rail_start.publish(self.rail_bool)
#             waypoint = Twist()
#             waypoint.linear.x = self.waypoints[self.current_waypoint_index][0]
#             waypoint.linear.y = self.waypoints[self.current_waypoint_index][1]
#             rad = self.waypoints[self.current_waypoint_index][2] * (3.14159 / 180)
#             waypoint.angular.z = rad  # Assuming z is not used for waypoints
            
#             self.waypoint_publisher.publish(waypoint)
            
#             self.get_logger().info(f'Published waypoint {self.current_waypoint_index + 1}: {waypoint.linear.x}, {waypoint.linear.y}')
#         else:
#             self.get_logger().info('All waypoints have been sent.')
#     def publish_retry_waypoint(self):
#         # self.get_logger().info(f'Publishing error {self.waypoints[self.current_waypoint_index][0]}')
#         if self.current_waypoint_index < len(self.waypoint_retry):
#             if self.current_waypoint_index == 3:
#                 self.rail_bool.data = True
#                 self.rail_start.publish(self.rail_bool)
#             waypoint = Twist()
#             waypoint.linear.x = self.waypoint_retry[self.current_waypoint_index][0]
#             waypoint.linear.y = self.waypoint_retry[self.current_waypoint_index][1]
#             rad = self.waypoint_retry[self.current_waypoint_index][2] * (3.14159 / 180)
#             waypoint.angular.z = rad  # Assuming z is not used for waypoints
            
#             self.waypoint_publisher.publish(waypoint)
            
#             self.get_logger().info(f'Published waypoint {self.current_waypoint_index + 1}: {waypoint.linear.x}, {waypoint.linear.y}')
#         else:
#             self.get_logger().info('All waypoints have been sent.')

#     def wp_done_callback(self, msg):
#         self.get_logger().info(f'Published waypoint {self.silo.silo}')
#         # if msg.done and self.current_waypoint_index != 0 and msg.error < self.waypoints[self.current_waypoint_index][2]:
#         #     self.get_logger().info(f'Waypoint {self.current_waypoint_index + 1} reached.')
#         #     self.publish_next_waypoint()
#         #     self.current_waypoint_index += 1
#         # elif msg.done and self.current_waypoint_index == 0 and msg.error < self.waypoints[self.current_waypoint_index][2]:
#         #     self.publish_next_waypoint()
#         #     self.current_waypoint_index += 1
# #####################################
#         if self.begin == 1:
#             if self.current_waypoint_index < len(self.waypoints):
#                 # if not msg.done and self.current_waypoint_index < len(self.waypoints) - 1:
#                 #     self.get_logger().info(f'Waypoint 3 going.')
#                 #     self.get_logger().info(f'Waypoint {self.current_waypoint_index + 1} reached.')
#                 #     self.publish_next_waypoint()
#                 #     self.current_waypoint_index += 1
#                 if not msg.done:
#                     self.get_logger().info(f'Start Zone.')
#                     self.get_logger().info(f'Waypoint 1 going.')
#                     self.publish_next_waypoint()
#                     if msg.error < self.waypoints[self.current_waypoint_index][3]:
#                         self.get_logger().info(f'Switch!!!!!!!!!!!!!!!!!!!!!!!!1')
#                         self.current_waypoint_index += 1        
#                 elif msg.done and self.current_waypoint_index == 0:
#                     self.get_logger().info(f'Waypoint 2 going.')
#                     self.publish_next_waypoint()
#                     # if msg.error < self.waypoints[self.current_waypoint_index][2]:
#                     #     self.current_waypoint_index += 1
#                 elif msg.done and self.current_waypoint_index != 0:
#                     self.get_logger().info(f'Waypoint 3 going.')
#                     self.get_logger().info(f'Waypoint {self.current_waypoint_index + 1} reached.')
#                     self.publish_next_waypoint()
#                     self.current_waypoint_index += 1
#             else:
#                 self.get_logger().info(f'Begin Object Detection.')
#                 self.begin = 3
#                 self.current_waypoint_index += 1
#         if self.begin == 2:
#             if self.current_waypoint_index < len(self.waypoint_retry):
#                 if not msg.done:
#                     self.get_logger().info(f'Retry Zone.')
#                     self.get_logger().info(f'Waypoint 1 going.')
#                     self.publish_retry_waypoint()
#                     if msg.error < self.waypoint_retry[self.current_waypoint_index][3]:
#                         self.get_logger().info(f'Switch!!!!!!!!!!!!!!!!!!!!!!!!')
#                         self.current_waypoint_index += 1
                    
#                 elif msg.done and self.current_waypoint_index == 0:
#                     self.get_logger().info(f'Waypoint 2 going.')
#                     self.publish_retry_waypoint()
#                     # if msg.error < self.waypoints[self.current_waypoint_index][2]:
#                     #     self.current_waypoint_index += 1
#                 elif msg.done and self.current_waypoint_index != 0:
#                     self.get_logger().info(f'Waypoint 3 going.')
#                     self.get_logger().info(f'Waypoint {self.current_waypoint_index + 1} reached.')
#                     self.publish_retry_waypoint()
#                     self.current_waypoint_index += 1
#             if self.current_waypoint_index == len(self.waypoint_retry):
#                 self.begin = 3
#                 self.current_waypoint_index += 1
#         ##########change to self.begin == 3############
#         if self.begin == 3:               
#             if self.limit_sw.grp_ball == True:
#                 self.get_logger().info(f'Published waypoint {self.target_b_x}: {self.target_b_y}, {self.target_b_z}')
#                 self.get_logger().info(f'drivesettled {msg.drive_settled}')
#                 self.waypoint.linear.x = (self.pos.x - self.target_b_x)
#                 # self.waypoint.linear.y = self.pos.y
#                 # self.waypoint.linear.x = self.pos.x
#                 self.waypoint.linear.y = self.pos.y
#                 self.waypoint.angular.z = self.target_b_z
#                 self.waypoint_publisher.publish(self.waypoint)
#                 if msg.drive_settled == True:
#                     self.settled_turn = False

#             # elif self.correct_ball.corr_ball == False and self.limit_sw.rail_btm == True:
#             elif self.limit_sw.grp_ball == False and self.ball_verify == True:
#                 if self.yellow_home == True:
#                     self.lidar_diff = self.lidar.data - SILO_DISTANCES[0]
#                     self.get_logger().info(f'Going back to zero yellow {self.pos.x}: {self.pos.y}')
#                     self.waypoint.linear.x = 0.0
#                     self.waypoint.linear.y = self.pos.y + self.lidar_diff
#                     self.waypoint.angular.z = 0.0
#                     self.waypoint_publisher.publish(self.waypoint)

#                 elif self.silo.silo != 0 and self.limit_sw._front_right == False and self.yellow_home == False:
#                     self.get_logger().info(f'Going to silo{self.pos.x}: {self.pos.y}')
#                     self.lidar_diff = self.lidar.data - SILO_DISTANCES[self.silo.silo]
#                     self.get_logger().info(f'update pos {self.pos.y}')
#                     self.waypoint.linear.x = 183.0
#                     self.waypoint.linear.y = self.pos.y + self.lidar_diff
#                     self.waypoint.angular.z =  0.0
#                     self.waypoint_publisher.publish(self.waypoint)
#                     print('lidar: ',self.lidar_diff)
#             elif self.ball_verify == False and self.limit_sw.rail_btm == True:
#                 self.get_logger().info(f'Going to yellow{self.pos.x}: {self.pos.y}')
#                 self.waypoint.linear.x = self.pos.x + 100.0
#                 self.waypoint.linear.y = 0.0
#                 self.waypoint.angular.z = 0.0
#                 self.waypoint_publisher.publish(self.waypoint)
#                 self.get_logger().info(f'Going to yellow{self.pos.x}: {self.pos.y}')
#                 self.smart_driver_send(7, 0.0)
#                 self.waypoint_publisher.publish(self.waypoint)
#         if self.begin == 4:
#             self.get_logger().info(f'Stop.')
#             self.waypoint.linear.x = 0.0
#             self.waypoint.linear.y = 0.0
#             self.waypoint.angular.z = 0.0
#             self.waypoint_publisher.publish(self.waypoint)
#             self.get_logger().info(f'Going to yellow{self.pos.x}: {self.pos.y}')
#             self.smart_driver_send(7, 0.0)
#             self.waypoint_publisher.publish(self.waypoint)

#     # def wp_done_callback(self, msg):
#     #     self.get_logger().info(f'Published waypoint {self.silo.silo}')
        
#     #     if self.begin == 1:
#     #         # Normal waypoint navigation
#     #         if self.current_waypoint_index < len(self.waypoints):
#     #             if not msg.done:
#     #                 self.get_logger().info(f'Start Zone. Waypoint 1 going.')
#     #                 self.publish_next_waypoint()
#     #                 if msg.error < self.waypoints[self.current_waypoint_index][3]:
#     #                     self.get_logger().info(f'Switch to next waypoint')
#     #                     self.current_waypoint_index += 1
#     #             elif msg.done and self.current_waypoint_index == 0:
#     #                 self.get_logger().info(f'Waypoint 2 going.')
#     #                 self.publish_next_waypoint()
#     #             elif msg.done and self.current_waypoint_index != 0:
#     #                 self.get_logger().info(f'Waypoint 3 going. Waypoint {self.current_waypoint_index + 1} reached.')
#     #                 self.publish_next_waypoint()
#     #                 self.current_waypoint_index += 1
#     #         else:
#     #             self.get_logger().info(f'Begin Object Detection.')
#     #             self.begin = 3
#     #             self.current_waypoint_index = 0  # Reset index for object detection waypoints

#     #     elif self.begin == 2:
#     #         # Retry waypoint navigation
#     #         if self.current_waypoint_index < len(self.waypoint_retry):
#     #             if not msg.done:
#     #                 self.get_logger().info(f'Retry Zone. Waypoint 1 going.')
#     #                 self.publish_retry_waypoint()
#     #                 if msg.error < self.waypoint_retry[self.current_waypoint_index][3]:
#     #                     self.get_logger().info(f'Switch to next retry waypoint')
#     #                     self.current_waypoint_index += 1
#     #             elif msg.done and self.current_waypoint_index == 0:
#     #                 self.get_logger().info(f'Waypoint 2 going.')
#     #                 self.publish_retry_waypoint()
#     #             elif msg.done and self.current_waypoint_index != 0:
#     #                 self.get_logger().info(f'Waypoint 3 going. Waypoint {self.current_waypoint_index + 1} reached.')
#     #                 self.publish_retry_waypoint()
#     #                 self.current_waypoint_index += 1
#     #         if self.current_waypoint_index == len(self.waypoint_retry):
#     #             self.begin = 3
#     #             self.current_waypoint_index = 0  # Reset index for object detection waypoints

#     #     elif self.begin == 3:
#     #         # Object detection and handling
#     #         self.get_logger().info(f'Object detection phase.')
#     #         if self.limit_sw.grp_ball:
#     #             self.get_logger().info(f'Moving to target waypoint {self.target_b_x}: {self.target_b_y}, {self.target_b_z}')
#     #             self.get_logger().info(f'Current position {self.pos.x}: {self.pos.y}')
#     #             self.waypoint.linear.x = self.target_b_x - self.pos.x
#     #             self.waypoint.linear.y = self.target_b_y - self.pos.y
#     #             self.waypoint.angular.z = self.target_b_z
#     #             self.waypoint_publisher.publish(self.waypoint)
#     #             self.get_logger().info(f'Published waypoint: {self.waypoint.linear.x}, {self.waypoint.linear.y}, {self.waypoint.angular.z}')
#     #             if msg.drive_settled:
#     #                 self.settled_turn = False

#     #         elif not self.limit_sw.grp_ball and self.ball_verify:
#     #             if self.yellow_home:
#     #                 self.lidar_diff = self.lidar.data - SILO_DISTANCES[0]
#     #                 self.get_logger().info(f'Going back to zero yellow {self.pos.x}: {self.pos.y}')
#     #                 self.waypoint.linear.x = 0.0
#     #                 self.waypoint.linear.y = self.pos.y + self.lidar_diff
#     #                 self.waypoint.angular.z = 0.0
#     #                 self.waypoint_publisher.publish(self.waypoint)

#     #             elif self.silo.silo != 0 and not self.limit_sw.front_right and not self.yellow_home:
#     #                 self.get_logger().info(f'Going to silo {self.pos.x}: {self.pos.y}')
#     #                 self.lidar_diff = self.lidar.data - SILO_DISTANCES[self.silo.silo]
#     #                 self.get_logger().info(f'update pos {self.pos.y}')
#     #                 self.waypoint.linear.x = 183.0
#     #                 self.waypoint.linear.y = self.pos.y + self.lidar_diff
#     #                 self.waypoint.angular.z = 0.0
#     #                 self.waypoint_publisher.publish(self.waypoint)
#     #                 self.get_logger().info(f'Published waypoint to silo: {self.waypoint.linear.x}, {self.waypoint.linear.y}, {self.waypoint.angular.z}')
#     #                 print('lidar: ', self.lidar_diff)

#     #         elif not self.ball_verify and self.limit_sw.rail_btm:
#     #             self.get_logger().info(f'Going to yellow {self.pos.x}: {self.pos.y}')
#     #             self.waypoint.linear.x = self.pos.x + 100.0
#     #             self.waypoint.linear.y = 0.0
#     #             self.waypoint.angular.z = 0.0
#     #             self.waypoint_publisher.publish(self.waypoint)
#     #             self.get_logger().info(f'Going to yellow {self.pos.x}: {self.pos.y}')
#     #             self.smart_driver_send(7, 0.0)
#     #             self.waypoint_publisher.publish(self.waypoint)

#     #     elif self.begin == 4:
#     #         # Stop all movement
#     #         self.get_logger().info(f'Stop.')
#     #         self.waypoint.linear.x = 0.0
#     #         self.waypoint.linear.y = 0.0
#     #         self.waypoint.angular.z = 0.0
#     #         self.waypoint_publisher.publish(self.waypoint)
#     #         self.get_logger().info(f'Going to yellow {self.pos.x}: {self.pos.y}')
#     #         self.smart_driver_send(7, 0.0)
#     #         self.waypoint_publisher.publish(self.waypoint)




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
#     node = WaypointProvider()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()


# if __name__ == '__main__':
#     main()
########################

import rclpy
import math

from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from cadt02_interfaces.msg import WayPoint, ArduinoFeedback, CameraFeedback, SmartDriver, Silo, LidarDist
from std_msgs.msg import Float32, Bool


SILO_DISTANCES = {
    1: 29.0,
    2: 105.0,
    3: 179.0,
    4: 254.0,
    5: 332.0,
    0: 179.0,
}


class WaypointProvider(Node):

    def __init__(self):
        super().__init__('waypoint_provider')

        # Publisher to send waypoints
        self.waypoint_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

        # Subscriber to get feedback from MovementControl
        self.create_subscription(WayPoint, 'wp_done', self.wp_done_callback, 10)
        self.create_subscription(Vector3, 'odometry', self.odometry_callback, 10)
        self.create_subscription(ArduinoFeedback, 'arduino_feedback', self.arduino_feedback_callback, 10)
        self.create_subscription(Twist, 'cmd_ball', self.cmd_ball_callback, 10)
        self.create_subscription(Silo, 'silo_num', self.silo_callback, 10)
        self.create_subscription(CameraFeedback, 'correct_ball', self.camera_feedback, 10)
        self.create_subscription(Vector3, 'orientation', self.orientation_callback, 10)
        self.create_subscription(LidarDist, '/publish_range', self.lidar_dist, 10)

        self.smart_driver_pub = self.create_publisher(SmartDriver, '/publish_motor', 10)
        self.rail_start = self.create_publisher(Bool, 'rail_start', 10)
        self.ball_bool = self.create_publisher(Bool, 'ball_caught', 10)
        self.team = self.create_publisher(Bool, 'team', 10)

        self.team_color = Bool()

        self.pos = Vector3()
        self.limit_sw = ArduinoFeedback()
        self.silo = Silo()
        self.lidar = LidarDist()
        self.rail_bool = Bool()
        self.way_point = WayPoint()
        self.lidar_diff = 0.0
        self.rail_bool.data = False

        #red
        self.waypoints = [(590.0, -20.0,0.0, 120.0, 0.0), (605.0, -435.0,0.0, 60.0, 0.0),(605.0 + 330,-435.0,0.0, 60.0, -1.0),(605.0 + 330,-435.0,90.0, 0.0, -1.0),(605.0 + 330,-180.0,90.0, 0.0, 0.0)]
        self.waypoint_retry = [(80.0, -20.0, 0.0, 20.0, 0.0), (90.0, -435.0, 0.0, 60.0, 0.0),
                               (90.0 + 330, -435.0, 0.0, 20.0, -1.0), (90.0 + 330, -435.0, 90.0, 0.0, -1.0)]
        # self.waypoints = [(200.0, 0.0, 0.0, 20.0), (200.0, 0.0, 90.0, 10.0)]

        #blue
        # self.waypoints = [(590.0, 20.0,0.0, 120.0, 0.0),(590.0, 20.0,0.0, 120.0, 0.0), (605.0, 435.0,0.0, 60.0, 0.0),(605.0 + 330.0,435.0,0.0, 60.0, -1.0),(605.0 + 330.0,435.0,-90.0, 0.0, -1.0),(605.0 + 330.0,180.0,-90.0, 0.0, 0.0)]
        # self.waypoint_retry = [(80.0, 20.0, 0.0, 20.0, 0.0), (90.0, 435.0, 0.0, 60.0, 0.0),
        #                        (90.0 + 330, 435.0, 0.0, 20.0), (90.0 + 330, 435.0, -90.0, 0.0, -1.0)]
        # self.waypoints = [(200.0, 0.0, 0.0, 20.0), (200.0, 0.0, 90.0, 10.0)]

        self.current_waypoint_index = 0
        self.sub_waypoint_index = 0  # New index to track x, y, omega stages
        self.waypoint = Twist()
        self.orientation = Vector3()
        self.correct_ball = CameraFeedback()
        self.silo_bool = Bool()

        self.position = None
        self.limit_sw.start = False

        self.begin = 0
        self.target_b_x = 0.0
        self.target_b_y = 0.0
        self.target_b_z = 0.0

        self.change_imu = 0.0
        self.settled_turn = False

        self.yellow_home = True
        self.ball_verify = False

    def camera_feedback(self, msg):
        self.correct_ball = msg
        if self.limit_sw.rail_btm:
            self.ball_verify = self.correct_ball.corr_ball

    def lidar_dist(self, msg):
        self.lidar = msg

    def silo_callback(self, msg):
        self.silo = msg
        if self.silo.silo != 0:
            self.yellow_home = False
        else:
            self.yellow_home = True

    def orientation_callback(self, msg):
        self.orientation = msg

    def cmd_ball_callback(self, msg):
        self.target_b_x = msg.linear.x
        self.target_b_y = msg.linear.y
        # theta = math.atan2(self.target_b_y, self.target_b_x)
        self.target_b_z = msg.angular.z

    def arduino_feedback_callback(self, msg):
        self.limit_sw = msg
        if self.limit_sw.grp_ball and self.limit_sw.front_right:
            self.yellow_home = True
        else:
            self.yellow_home = False

        if self.limit_sw.start:
            self.begin = 1
        if self.limit_sw.retry:
            self.begin = 2
        if self.limit_sw.mode:
            self.begin = 4

    def odometry_callback(self, msg):
        self.pos = msg

    # def publish_next_waypoint(self):
    #      # self.get_logger().info(f'Publishing error {self.waypoints[self.current_waypoint_index][0]}')
    #     if self.current_waypoint_index < len(self.waypoint_retry):
    #         if self.current_waypoint_index == 1:
    #             self.rail_bool.data = True
    #             self.rail_start.publish(self.rail_bool)
    #         waypoint = Twist()
    #         waypoint.linear.x = self.waypoint_retry[self.current_waypoint_index][0]
    #         waypoint.linear.y = self.waypoint_retry[self.current_waypoint_index][1]
    #         rad = self.waypoint_retry[self.current_waypoint_index][2] * (3.14159 / 180)
    #         waypoint.angular.z = rad  # Assuming z is not used for waypoints
            
    #         self.waypoint_publisher.publish(waypoint)
            
    #         self.get_logger().info(f'Published waypoint {self.current_waypoint_index + 1}: {waypoint.linear.x}, {waypoint.linear.y}')
    #     else:
    #         self.get_logger().info('All waypoints have been sent.')
    # def publish_retry_waypoint(self):
    #     # self.get_logger().info(f'Publishing error {self.waypoints[self.current_waypoint_index][0]}')
    #     if self.current_waypoint_index < len(self.waypoint_retry):
    #         if self.current_waypoint_index == 3:
    #             self.rail_bool.data = True
    #             self.rail_start.publish(self.rail_bool)
    #         waypoint = Twist()
    #         waypoint.linear.x = self.waypoint_retry[self.current_waypoint_index][0]
    #         waypoint.linear.y = self.waypoint_retry[self.current_waypoint_index][1]
    #         rad = self.waypoint_retry[self.current_waypoint_index][2] * (3.14159 / 180)
    #         waypoint.angular.z = rad  # Assuming z is not used for waypoints
            
    #         self.waypoint_publisher.publish(waypoint)
            
    #         self.get_logger().info(f'Published waypoint {self.current_waypoint_index + 1}: {waypoint.linear.x}, {waypoint.linear.y}')
    #     else:
    #         self.get_logger().info('All waypoints have been sent.')
    def publish_next_waypoint(self):
                # self.get_logger().info(f'Publishing error {self.waypoints[self.current_waypoint_index][0]}')
        if self.current_waypoint_index < len(self.waypoints):
            if self.current_waypoint_index == 3:
                self.rail_bool.data = True
                self.rail_start.publish(self.rail_bool)

            self.get_logger().info(f'self.waypoints[self.current_waypoint_index].{self.waypoints[self.current_waypoint_index]}')
            waypoint = Twist()
            waypoint.linear.x = self.waypoints[self.current_waypoint_index][0]
            waypoint.linear.y = self.waypoints[self.current_waypoint_index][1]
            rad = self.waypoints[self.current_waypoint_index][2] * (3.14159 / 180)
            waypoint.angular.z = rad  # Assuming z is not used for waypoints
            waypoint.linear.z = self.waypoints[self.current_waypoint_index][4]
            
            self.waypoint_publisher.publish(waypoint)
            
            self.get_logger().info(f'Published waypoint {self.current_waypoint_index + 1}: {waypoint.linear.x}, {waypoint.linear.y}')
        else:
            self.get_logger().info('All waypoints have been sent.')
    def publish_retry_waypoint(self):
        if self.current_waypoint_index < len(self.waypoint_retry):
            if self.current_waypoint_index == 1:
                self.rail_bool.data = True
                self.rail_start.publish(self.rail_bool)
            waypoint = Twist()
            waypoint.linear.x = self.waypoint_retry[self.current_waypoint_index][0]
            waypoint.linear.y = self.waypoint_retry[self.current_waypoint_index][1]
            rad = self.waypoint_retry[self.current_waypoint_index][2] * (3.14159 / 180)
            waypoint.angular.z = rad  # Assuming z is not used for waypoints
            waypoint.linear.z = self.waypoint_retry[self.current_waypoint_index][4]
            
            self.waypoint_publisher.publish(waypoint)
            
            self.get_logger().info(f'Published waypoint {self.current_waypoint_index + 1}: {waypoint.linear.x}, {waypoint.linear.y}')
        else:
            self.get_logger().info('All waypoints have been sent.')
    def wp_done_callback(self, msg):
        ####open fo Blue
        self.team_color.data = True
        ###Open for red
        # self.team_color.data = False
        self.team.publish(self.team_color)
        self.way_point = msg
        self.get_logger().info(f'Waypoint {self.current_waypoint_index + 1} reached with status done={msg.done} and error={msg.error}')

        if self.begin == 1:  # Normal waypoint navigation
            # self.handle_object_detection(msg)
            self.handle_normal_navigation(msg)
        elif self.begin == 2:  # Retry waypoint navigation
            self.handle_retry_navigation(msg)
        elif self.begin == 3:  # Object detection and handling
            self.handle_object_detection(msg)
        elif self.begin == 4:  # Stop all movement
            self.handle_stop(msg)
        #self.handle_normal_navigation(msg)
        # if self.begin == 1:
        #     self.rail_bool.data = True
        #     self.rail_start.publish(self.rail_bool)
        #     self.handle_object_detection(msg)

    def handle_normal_navigation(self, msg):
            if not msg.done:
                self.get_logger().info(f'Waypoint 1 going.')
                self.publish_next_waypoint()
                self.get_logger().info(f'not chnaging.')
                self.get_logger().info(f'msg.error.{msg.error}')
                # self.get_logger().info(f'self.waypoints[self.current_waypoint_index][3].{self.waypoints[self.current_waypoint_index][4]}')
                
                if msg.error < self.waypoints[self.current_waypoint_index][3]:
                    self.get_logger().info(f'chnaging.')
                    self.current_waypoint_index += 1
                    if self.current_waypoint_index == (len(self.waypoints) - 1):
                        self.begin = 3
                    # self.current_waypoint_index += 1
            elif msg.done and self.current_waypoint_index == 0:
                self.get_logger().info(f'Waypoint 2 going.')
                self.publish_next_waypoint()
                # if msg.error < self.waypoints[self.current_waypoint_index][2]:
                #     self.current_waypoint_index += 1
            elif msg.done and self.current_waypoint_index != 0:
                self.get_logger().info(f'Waypoint 3 going.')
                self.get_logger().info(f'Waypoint {self.current_waypoint_index + 1} reached.')
                self.publish_next_waypoint()
                self.current_waypoint_index += 1
            if self.current_waypoint_index == (len(self.waypoints) - 1):
                self.begin = 3

    def handle_retry_navigation(self, msg):
            if not msg.done:
                self.get_logger().info(f'Waypoint 1 going.')
                self.publish_next_waypoint()
                if msg.error < self.waypoints[self.current_waypoint_index][3]:
                    self.current_waypoint_index += 1
                    if self.current_waypoint_index == (len(self.waypoints) - 1):
                        self.begin = 3
                    # self.current_waypoint_index += 1
            elif msg.done and self.current_waypoint_index == 0:
                self.get_logger().info(f'Waypoint 2 going.')
                self.publish_next_waypoint()
                # if msg.error < self.waypoints[self.current_waypoint_index][2]:
                #     self.current_waypoint_index += 1
            elif msg.done and self.current_waypoint_index != 0:
                self.get_logger().info(f'Waypoint 3 going.')
                self.get_logger().info(f'Waypoint {self.current_waypoint_index + 1} reached.')
                self.publish_next_waypoint()
                self.current_waypoint_index += 1

            if self.current_waypoint_index == (len(self.waypoints) - 1):
                self.begin = 3

    def handle_object_detection(self, msg):
        self.get_logger().info(f'Object detection phase. Waypoint {self.current_waypoint_index + 1}')
        if self.limit_sw.grp_ball:
            self.move_to_target_ball(msg)
        elif not self.limit_sw.grp_ball:
            self.move_to_silo_or_home(msg)
        elif not self.ball_verify and self.limit_sw.rail_btm:
            self.move_to_yellow_home(msg)

    def handle_stop(self, msg):
        self.get_logger().info('Stop. Halting all movements.')
        self.waypoint.linear.x = 0.0
        self.waypoint.linear.y = 0.0
        self.waypoint.angular.z = 0.0
        self.waypoint_publisher.publish(self.waypoint)
        self.smart_driver_send(7, 0.0)

    def move_to_target_ball(self, msg):
        
        self.waypoint.linear.x =  self.pos.x - self.target_b_x
        # self.waypoint.linear.x =  0.0
        # self.waypoint.linear.y =  self.pos.y- self.target_b_y
        self.waypoint.linear.y = 0.0
        self.waypoint.angular.z = self.target_b_z
        # self.waypoint.angular.z = 0.0
        self.waypoint.linear.z = -1.0
        self.get_logger().info(f'Moving to target waypoint {self.waypoint.linear.x}: {self.waypoint.linear.y}, {self.waypoint.angular.z}')
        self.waypoint_publisher.publish(self.waypoint)
        if self.way_point.drive_settled:
            self.settled_turn = False

    def move_to_silo_or_home(self, msg):
        if self.yellow_home:
            self.lidar_diff = self.lidar.y - SILO_DISTANCES[0]
            self.get_logger().info(f'Going back to zero yellow {self.pos.x}: {self.pos.y}')
            diff = self.lidar.verify - self.lidar.y
            if -5 < diff < 5:
                self.waypoint.linear.x = self.pos.x + 200
            else:
                self.waypoint.linear.x = self.pos.x + 300
            # self.waypoint.linear.y = self.pos.y + self.lidar_diff
            self.waypoint.linear.y = SILO_DISTANCES[0]
            self.waypoint.angular.z = 0.0
            self.waypoint_publisher.publish(self.waypoint)
        elif self.silo.silo != 0 and not self.limit_sw.front_right and not self.yellow_home:
            self.lidar_diff = self.lidar.y - SILO_DISTANCES[self.silo.silo]
            self.get_logger().info(f'Going to silo {self.pos.x}: {self.pos.y}')
            self.waypoint.linear.x = 183.0
            # self.waypoint.linear.y = self.pos.y + self.lidar_diff
            self.waypoint.linear.y = SILO_DISTANCES[self.silo.silo]
            self.waypoint.angular.z = 0.0
            self.waypoint_publisher.publish(self.waypoint)
            self.silo_bool.data = True
            self.ball_bool.publish(self.silo_bool)

    def move_to_yellow_home(self, msg):
        self.get_logger().info(f'Going to yellow home {self.pos.x}: {self.pos.y}')
        self.waypoint.linear.x = self.pos.x + 200.0
        self.waypoint.linear.y = 0.0
        self.waypoint.angular.z = 3.14
        self.waypoint_publisher.publish(self.waypoint)
        self.smart_driver_send(7, 0.0)

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
    node = WaypointProvider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
