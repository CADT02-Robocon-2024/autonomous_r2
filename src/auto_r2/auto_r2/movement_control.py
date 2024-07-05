import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from cadt02_interfaces.msg import WayPoint, ArduinoFeedback


class WaypointProvider(Node):

    def __init__(self):
        super().__init__('waypoint_provider')

        # Publisher to send waypoints
        self.waypoint_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

        # Subscriber to get feedback from MovementControl
        self.create_subscription(WayPoint, 'wp_done', self.wp_done_callback, 10)
        self.create_subscription(Vector3, 'odometry', self.odometry_callback, 10)
        self.create_subscription(ArduinoFeedback, 'arduino_feedback', self.arduino_feedback_callback, 10)

    
        self.pos = Vector3()

        # Define waypoints
        # self.waypoints = []
        self.waypoints = [(570.0, 0.0,0.0, 110.0), (570.0, -385.0,0.0, 60.0),(570.0 + 290,-385.0,0.0, 20.0),(570.0 + 290,-385.0,90.0, 0.0),(self.pos.x - 390.0, self.pos.y, 90.0, 0.0)]
        # self.waypoints = [(0.0, -400.0, 60.0),(330.0,-400.0, 0.0)]
        # self.waypoints = [(330.0, 0.0, 0.0, 20.0),(330.0, 0.0, 90.0, 0.0),(self.pos.x - 380.0, self.pos.y, 90.0, 0.0)]
        self.current_waypoint_index = 0

        # Publish the first waypoint
        # self.publish_next_waypoint()
        self.rail_btm = None
        self.rail_top = None
        self.grp_ball = None
        self.position = None
        self.begin = 0

    def arduino_feedback_callback(self, msg):
        self.rail_btm = msg.rail_btm
        self.rail_top = msg.rail_top
        self.grp_ball = msg.grp_ball
        self.start = msg.start

        if self.start:
            self.begin = 1


    def odometry_callback(self, msg):
        self.pos = msg
        self.waypoints = [(570.0, 0.0,0.0, 110.0), (570.0, -385.0,0.0, 60.0),(570.0 + 290,-385.0,0.0, 20.0),(570.0 + 290,-385.0,90.0, 0.0),(self.pos.x - 390.0, self.pos.y, 90.0, 0.0)]
        # self.waypoints = [(0.0, -400.0, 60.0),(330.0,-400.0, 0.0)]
        # self.waypoints = [(330.0, 0.0, 0.0, 20.0),(330.0, 0.0, 90.0, 0.0),(self.pos.x - 380.0, self.pos.y, 90.0, 0.0)]
        

    def publish_next_waypoint(self):
        # self.get_logger().info(f'Publishing error {self.waypoints[self.current_waypoint_index][0]}')
        if self.current_waypoint_index < len(self.waypoints):
            waypoint = Twist()
            waypoint.linear.x = self.waypoints[self.current_waypoint_index][0]
            waypoint.linear.y = self.waypoints[self.current_waypoint_index][1]
            rad = self.waypoints[self.current_waypoint_index][2] * (3.14159 / 180)
            waypoint.angular.z = rad  # Assuming z is not used for waypoints
            
            self.waypoint_publisher.publish(waypoint)
            
            self.get_logger().info(f'Published waypoint {self.current_waypoint_index + 1}: {waypoint.linear.x}, {waypoint.linear.y}')
        else:
            self.get_logger().info('All waypoints have been sent.')

    def wp_done_callback(self, msg):
        # if msg.done and self.current_waypoint_index != 0 and msg.error < self.waypoints[self.current_waypoint_index][2]:
        #     self.get_logger().info(f'Waypoint {self.current_waypoint_index + 1} reached.')
        #     self.publish_next_waypoint()
        #     self.current_waypoint_index += 1
        # elif msg.done and self.current_waypoint_index == 0 and msg.error < self.waypoints[self.current_waypoint_index][2]:
        #     self.publish_next_waypoint()
        #     self.current_waypoint_index += 1

        if self.begin == 1:
            if not msg.done:
                self.get_logger().info(f'Waypoint 1 going.')
                self.publish_next_waypoint()
                if msg.error < self.waypoints[self.current_waypoint_index][3]:
                    self.current_waypoint_index += 1
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
            


def main(args=None):
    rclpy.init(args=args)
    node = WaypointProvider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
