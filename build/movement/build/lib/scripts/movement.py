import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from movement.rmd_motors import run_speed

class MoveNode(Node):
    def __init__(self):
        super().__init__('move_node')
        self.subscription = self.create_subscription(
            Vector3,
            'velocity_command',
            self.velocity_command_callback,
            10
        )
        self.get_logger().info('MoveNode has been started.')

    def velocity_command_callback(self, msg):
        self.get_logger().info(f'Received velocity command: x={msg.x}, y={msg.y}, angular.z={msg.z}')
        self.move(msg.x, msg.y, msg.z)

    def move(self, Vx, Vy, omega):
        l = 25
        a = l / 1.41
        b = l / 1.41
        r = 6.35
        M = [0, 0, 0, 0]
        M[0] = (Vx - Vy - (a + b) * omega) / r
        M[1] = (Vx + Vy + (a + b) * omega) / r
        M[2] = (Vx - Vy + (a + b) * omega) / r
        M[3] = (Vx + Vy - (a + b) * omega) / r

        self.get_logger().info(f'Motor speeds: {M[0]}, {M[1]}, {M[2]}, {M[3]}')
        
        run_speed(1, M[0])
        run_speed(2, -M[1])
        run_speed(3, -M[2])
        run_speed(4, M[3])

def main(args=None):
    rclpy.init(args=args)
    node = MoveNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
