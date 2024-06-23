import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from cadt02_interfaces.msg import WayPoint


class WaypointProvider(Node):

    def __init__(self):
        super().__init__('waypoint_provider')

        # Publisher to send waypoints
        self.waypoint_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

        # Subscriber to get feedback from MovementControl
        self.create_subscription(WayPoint, 'wp_done', self.wp_done_callback, 10)
        self.create_subscription(Vector3, 'odometry', self.odometry_callback, 10)
    
        self.pos = Vector3()

        # Define waypoints
        # self.waypoints = []
        self.waypoints = [(590.0, 0.0, 50.0), (self.pos.x, -370.0, 0.0),(self.pos.x + 340,-370.0, 0.0)]
        self.current_waypoint_index = 0

        # Publish the first waypoint
        self.publish_next_waypoint()
    def odometry_callback(self, msg):
        self.pos = msg
        self.waypoints = [(590.0, 0.0, 50.0), (self.pos.x, -370.0, 0.0),(self.pos.x + 340,-370.0, 0.0)]
        

    def publish_next_waypoint(self):
        # self.get_logger().info(f'Publishing error {self.waypoints[self.current_waypoint_index][0]}')
        if self.current_waypoint_index < len(self.waypoints):
            waypoint = Twist()
            waypoint.linear.x = self.waypoints[self.current_waypoint_index][0]
            waypoint.linear.y = self.waypoints[self.current_waypoint_index][1]
            waypoint.angular.z = 0.0  # Assuming z is not used for waypoints
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
        if not msg.done:
            # self.get_logger().info(f'Waypoint {self.current_waypoint_index + 1} reached.')
            self.publish_next_waypoint()
            if msg.error <= self.waypoints[self.current_waypoint_index][2]:
                self.current_waypoint_index += 1
        elif msg.done and self.current_waypoint_index == 0:
            self.publish_next_waypoint()
            if msg.error <= self.waypoints[self.current_waypoint_index][2]:
                self.current_waypoint_index += 1
        elif msg.done and self.current_waypoint_index != 0:
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
