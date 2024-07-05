import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from cadt02_interfaces.msg import WayPoint


class WaypointProvider(Node):

    def __init__(self):
        super().__init__('waypoint_provider')

        # Publisher to send waypoints
        self.waypoint_publisher = self.create_publisher(Vector3, 'cmd_vel', 10)

        # Subscriber to get feedback from MovementControl
        self.create_subscription(WayPoint, 'wp_done', self.wp_done_callback, 10)

        # Define waypoints
        self.waypoints = [(100.0, 0.0), (100.0, 100.0)]
        self.current_waypoint_index = 0

        # Publish the first waypoint
        self.publish_next_waypoint()

    def publish_next_waypoint(self):
        if self.current_waypoint_index < len(self.waypoints):
            waypoint = Vector3()
            waypoint.x = self.waypoints[self.current_waypoint_index][0]
            waypoint.y = self.waypoints[self.current_waypoint_index][1]
            waypoint.z = 0.0  # Assuming z is not used for waypoints
            self.waypoint_publisher.publish(waypoint)
            self.get_logger().info(f'Published waypoint {self.current_waypoint_index + 1}: {waypoint.x}, {waypoint.y}')
        else:
            self.get_logger().info('All waypoints have been sent.')

    def wp_done_callback(self, msg):
        if msg.done:
            self.get_logger().info(f'Waypoint {self.current_waypoint_index + 1} reached.')
            self.current_waypoint_index += 1
            self.publish_next_waypoint()


def main(args=None):
    rclpy.init(args=args)
    node = WaypointProvider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
