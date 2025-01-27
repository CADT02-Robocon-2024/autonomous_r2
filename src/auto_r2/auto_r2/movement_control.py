"""
    This code controls the path planning of the Robot 2 from Area 1 to Area 3. This code only works for the red team.
"""
import rclpy
import math

from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from cadt02_interfaces.msg import WayPoint, ArduinoFeedback, CameraFeedback, SmartDriver, Silo, LidarDist
from std_msgs.msg import Float32, Bool

# the silo distances from the wall to the L515
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

        # Subscriber
        
        # when the waypoint is reached (odometry_cont)
        self.create_subscription(WayPoint, 'wp_done', self.wp_done_callback, 10)
        # the position of the robot (odometry_cont)
        self.create_subscription(Vector3, 'odometry', self.odometry_callback, 10)
        # feedback get the limit switches status (arduino_feedback)
        self.create_subscription(ArduinoFeedback, 'arduino_feedback', self.arduino_feedback_callback, 10)
        # feedback from the camera to get the ball position (live_dection_node)
        self.create_subscription(Twist, 'cmd_ball', self.cmd_ball_callback, 10)
        # feedback from the silo to get the silo number from the other pc(smart_driver)
        self.create_subscription(Silo, 'silo_num', self.silo_callback, 10)
        # feedback from the camera if the ball grabbed is correct (live_dection_node)
        self.create_subscription(CameraFeedback, 'correct_ball', self.camera_feedback, 10)
        # # feedback from the imu to get the orientation of the robot (imu_cont)
        # self.create_subscription(Vector3, 'orientation', self.orientation_callback, 10)
        
        # feedback from the L515 to get the distance from the wall (get_dist)
        self.create_subscription(LidarDist, '/publish_range', self.lidar_dist, 10)
        
        # Publisher 
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
        """
        The `camera_feedback` function sets the correct ball based on a message and verifies it if a limit
        switch is triggered.
        
        :param msg: It takes 'msg' as a parameter which is a CameraFeedback message. It notify if the ball is correct based on the team's color.
        """
        self.correct_ball = msg
        if self.limit_sw.rail_btm:
            self.ball_verify = self.correct_ball.corr_ball

    def lidar_dist(self, msg):
        """
        The `lidar_dist` function gets the distance of the Lidar from the L515.
        
        :param msg: Get the distance from the node get_dist.
        """
        self.lidar = msg

    def silo_callback(self, msg):
        """
        The `silo_callback` function updates whether the robot is at the yellow home or not.
        
        :param msg: In the `silo_callback` method, the `msg` parameter is being used to update the
        `self.silo` attribute based on the value of `msg.silo`. If `msg.silo` is not equal to 0, then
        `self.yellow_home` is set to `False.
        """
        self.silo = msg
        if self.silo.silo != 0:
            self.yellow_home = False
        else:
            self.yellow_home = True

    def orientation_callback(self, msg):
        """
        The `orientation_callback` function in Python updates the `orientation` attribute with the provided by the IMU.
        """
        self.orientation = msg

    def cmd_ball_callback(self, msg):
        """
        The `cmd_ball_callback` function updates the target ball coordinates and orientation based on the
        received message.
        
        :param msg: The msg is recieved from the camera_feedback node. It is a Twist message that contains the x, y, and z coordinates of the target ball.
        """
        self.target_b_x = msg.linear.x
        self.target_b_y = msg.linear.y
        # theta = math.atan2(self.target_b_y, self.target_b_x)
        self.target_b_z = msg.angular.z

    def arduino_feedback_callback(self, msg):
        """
        The `arduino_feedback_callback` function updates the mode of the robot based on the button.
        
        :param msg: msg is the feedback from the Arduino node. It is an ArduinoFeedback message that contains the status of the limit switches and buttons.
        """
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
        """
        The `odometry_callback` function stores the position of the robot in the `pos` attribute of the
        class.
        
        :param msg: The `msg` parameter in the `odometry_callback` function is typically a message
        containing information about the robot's position and orientation. This information is usually
        obtained from sensors such as encoders or IMU (Inertial Measurement Unit) and is used for
        localization and navigation purposes in robotics applications
        """
        self.pos = msg

    def publish_next_waypoint(self):
        """
        This function publishes the next waypoint for a robot to follow along a predefined path.
        """
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
        """
        This Python function publishes waypoints with retry logic based on a given list of coordinates and
        angles.
        """
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
        # The above Python code snippet is a part of a larger program that appears to be a navigation system
        # for a robot or autonomous vehicle. Here is a breakdown of the code:
        
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

    def handle_normal_navigation(self, msg):
        """
        The function `handle_normal_navigation` processes messages to navigate through waypoints, updating
        the current waypoint index based on certain conditions.
        
        :param msg: It seems like the code snippet you provided is a method named `handle_normal_navigation`
        that takes `self` and `msg` as parameters. The method contains logic to handle navigation based on
        the `msg` parameter
        """
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
        """
        The function `handle_retry_navigation` manages waypoint navigation and progression based on certain
        conditions.
        
        """
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
        """
        The function `handle_object_detection` determines the robot's position based on the soli number.
        
        :param msg: The `handle_object_detection` method is checking certain conditions based
        on the values of `self.limit_sw.grp_ball`, `self.ball_verify`, and `self.limit_sw.rail_btm` to
        determine the next action to take in the object detection phase
        """
        self.get_logger().info(f'Object detection phase. Waypoint {self.current_waypoint_index + 1}')
        if self.limit_sw.grp_ball:
            self.move_to_target_ball(msg)
        elif not self.limit_sw.grp_ball:
            self.move_to_silo_or_home(msg)
        elif not self.ball_verify and self.limit_sw.rail_btm:
            self.move_to_yellow_home(msg)

    def handle_stop(self, msg):
        """
        The `handle_stop` function stops all movements and halts the robot.
        
        :param msg: The `handle_stop` method is a function that handles a stop message. When this method is
        called, it logs a message indicating that all movements should halt, sets the linear and angular
        velocities of the `waypoint` to zero, publishes the updated `waypoint` message, and sends a command
        """
        self.get_logger().info('Stop. Halting all movements.')
        self.waypoint.linear.x = 0.0
        self.waypoint.linear.y = 0.0
        self.waypoint.angular.z = 0.0
        self.waypoint_publisher.publish(self.waypoint)
        self.smart_driver_send(7, 0.0)

    def move_to_target_ball(self, msg):
        """
        The function `move_to_target_ball` calculates the movement required to reach a target ball and
        publishes the calculated waypoint.
        
        :param msg: The `move_to_target_ball` method is trying to calculate the movement
        required to reach a target ball based on the current position and target coordinates. The parameters
        `self.pos`, `self.target_b_x`, `self.target_b_y`, and `self.target_b_z` are used in
        """
        
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
        """
        This function moves a robot to a silo or back to its home position based on certain conditions.
        
        :param msg: It seems like the `msg` parameter is defined in the function signature
        `move_to_silo_or_home(self, msg)`, but it is not being used within the function body. If you
        intended to use this parameter for some specific functionality within the `move_to_silo_or_home`
        method,
        """
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
        """
        This Python function moves a robot to a yellow home location by setting specific waypoint
        coordinates and publishing them.
        
        :param msg: It looks like the `move_to_yellow_home` function is designed to move a robot to a
        specific location representing a yellow home. The function logs a message indicating the intention
        to go to the yellow home at the current position `(self.pos.x, self.pos.y)`
        """
        self.get_logger().info(f'Going to yellow home {self.pos.x}: {self.pos.y}')
        self.waypoint.linear.x = self.pos.x + 200.0
        self.waypoint.linear.y = 0.0
        self.waypoint.angular.z = 3.14
        self.waypoint_publisher.publish(self.waypoint)
        self.smart_driver_send(7, 0.0)

    def smart_driver_send(self, mid, goal, stop=False):
        """
        The `smart_driver_send` function publishes the commands for the gripper via smart driver.
        
        :param mid: motor id
        :param goal: The goal position of the motor
        :param stop: The `stop` parameter in the `smart_driver_send` function is a boolean parameter that
        indicates whether the smart driver should stop or not. If `stop` is set to `True`, it means the
        smart driver should stop, and if it is set to `False`, it means the smart driver, defaults to False
        (optional)
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
    node = WaypointProvider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
