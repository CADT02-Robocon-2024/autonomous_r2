import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Imu
import math
from odometry.PID import PID


# class PID:
#     def __init__(self, setpoint, kp, ki, kd=0, tolerance=0):
#         self.setpoint = setpoint
#         self.kp = kp
#         self.ki = ki
#         self.kd = kd
#         self.tolerance = tolerance
#         self.prev_error = 0
#         self.integral = 0

#     def calculate_pid_output(self, current_value):
#         error = self.setpoint - current_value
#         self.integral += error
#         derivative = error - self.prev_error
#         self.prev_error = error
#         output = self.kp * error + self.ki * self.integral + self.kd * derivative
#         return output

#     def is_settled(self):
#         return abs(self.prev_error) < self.tolerance


class MovementControl(Node):

    def __init__(self):
        super().__init__('movement_control')

        # Subscriptions
        self.create_subscription(Vector3, 'odometry', self.odometry_callback, 10)
        self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        self.create_subscription(Imu, 'imu/data_raw', self.imu_callback, 10)

        # Publisher
        self.velocity_publisher = self.create_publisher(Vector3, 'velocity_command', 10)

        # Initialize positions
        self.pos = Vector3()
        self.imu = Imu()
        self.orientation = 0.0
        self.target_x = 0.0
        self.target_y = 0.0
        self.target_heading = 0.0

        self.imu_counter = 0
        self.offset_w = 0
        self.corrected_yaw = 0.0

        # Timer
        self.timer = self.create_timer(0.1, self.movement)

        self.move = True

        # Initialize PID controllers
        self.driveOutput = PID(0, 2, 0, 10, 20)
        self.turnOutput = PID(0, 2, 0, 0.03, 10)
        self.driveVx = PID(0, 35, 0)
        self.driveVy = PID(0, 35, 0)
        self.turnPID = PID(0, 50, 0)

    def odometry_callback(self, msg):
        self.pos = msg
    
    def imu_callback(self, msg):
        self.imu = msg
        if self.imu_counter == 0:
            self.offset_w = self.imu.orientation.w
            self.get_logger().info(f'self.offset_w: {self.offset_w}')
            self.imu_counter = 1

        if self.imu.orientation.w < math.pi:
            if self.offset_w > math.pi:
                self.corrected_yaw = self.imu.orientation.w + (2*math.pi - self.offset_w)
            else:
                self.corrected_yaw = (self.offset_w - self.imu.orientation.w) * -1
        else:
            if self.offset_w > math.pi:
                self.corrected_yaw = (self.imu.orientation.w - self.offset_w)
            else: 
                self.corrected_yaw = (self.offset_w + (2*math.pi - self.imu.orientation.w)) * -1

    def cmd_vel_callback(self, msg):
        self.target_x = msg.linear.x
        self.target_y = msg.linear.y
        self.target_heading = msg.angular.z

    def moving(self):
        targets = [self.target_x, self.target_y, self.target_heading]
        self.get_logger().info(f'targets: {targets}')
        while self.move:
            self.get_logger().info(f'moving')
            self.movement(self.target_x, self.target_y, self.target_heading)
            self.move = False
        
        self.get_logger().info(f'Move complete')

    def clamp(input_value, min_value, max_value):
        if input_value > max_value:
            return max_value
        if input_value < min_value:
            return min_value
        return input_value


    def movement(self):
        print('Hello')
        turnOutput_PID = self.turnOutput.calculate_pid_output((self.target_heading) - (self.corrected_yaw))
        driveOutput_PID = self.driveOutput.calculate_pid_output(math.hypot(self.target_x - self.pos.x, self.target_y - self.pos.y))

        turnSettled = self.turnOutput.is_settled()
        self.get_logger().info(f'error {(self.target_heading) - (self.corrected_yaw)}')
        self.get_logger().info(f'orientation {(self.corrected_yaw)}')
        self.get_logger().info(f'Offset {(self.offset_w)}')
        self.driveOutput.setpoint = math.hypot(self.target_x - self.pos.x, self.target_y - self.pos.y)
        self.driveVx.setpoint = self.target_x - self.pos.x
        self.driveVy.setpoint = self.target_y - self.pos.y
        self.turnPID.setpoint = (self.target_heading) - (self.corrected_yaw)

        if not self.driveOutput.is_settled() or not turnSettled:
            turnSettled = self.turnOutput.is_settled()
            self.get_logger().info(f'target x {turnSettled}')
            error_x = self.target_x - self.pos.x
            error_y = self.target_y - self.pos.y
            heading_error = (self.target_heading) - (self.corrected_yaw)

            theta2 = math.atan2(error_y, error_x)

            Vy = (math.cos(theta2) - math.sin(theta2))
            Vx = (math.sin(theta2) + math.cos(theta2))

            Vx_PID = self.driveVx.calculate_pid_output(error_x)
            Vy_PID = self.driveVy.calculate_pid_output(error_y)
            omega_PID = self.turnPID.calculate_pid_output(heading_error)

            Vx = (Vx_PID + Vx)
            Vy = -1 * (Vy_PID + Vy)
            omega = -1 *omega_PID

            Vx = max(min(Vx, 4800), -4800)
            Vy = max(min(Vy, 4800), -4800)
            if omega < 10 and omega > 0:
                omega = 10.0
            elif omega > -10 and omega < 0:
                omega = -10.0
            


            if (self.target_heading) != 0 and self.target_x == 0 and self.target_y == 0:
                Vx = 0.0
                Vy = 0.0
                self.get_logger().info("Rotation")

            else:
                # turnSettled = True
                self.get_logger().info("Linear")

            velocity_command = Vector3()
            velocity_command.x = Vx
            print(f'Type: {type(omega)}')
            velocity_command.y = Vy
            velocity_command.z = omega

            self.velocity_publisher.publish(velocity_command)
            self.get_logger().info(f'Publishing velocity: Vx={Vx}, Vy={Vy}, omega={omega}')
        elif self.driveOutput.is_settled() or turnSettled:
            self.get_logger().info("Settled")
            velocity_command = Vector3()
            velocity_command.x = 0.0
            velocity_command.y = 0.0
            velocity_command.z = 0.0
            self.velocity_publisher.publish(velocity_command)


def main(args=None):
    rclpy.init(args=args)
    node = MovementControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()