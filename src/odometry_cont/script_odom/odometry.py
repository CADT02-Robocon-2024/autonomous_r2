import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Float32, Bool
from sensor_msgs.msg import Imu
import math
from odometry_cont.PID import PID
from cadt02_interfaces.msg import WayPoint, LidarDist


class MovementControl(Node):

    def __init__(self):
        super().__init__('movement_control')

        # Subscriptions
        self.create_subscription(Vector3, 'odometry', self.odometry_callback, 10)
        self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        self.create_subscription(Imu, 'imu/data_raw', self.imu_callback, 10)
        # self.create_subscription(Float32, 'publish_range', self.lidar_dist, 10)
        self.create_subscription(LidarDist, '/publish_range', self.lidar_dist, 10)

        # Publisher
        self.velocity_publisher = self.create_publisher(Vector3, 'velocity_command', 10)
        self.way_point_bool = self.create_publisher(WayPoint, 'wp_done', 10)
        self.create_subscription(Bool, 'team_color', self.team_color_callback, 10)
        
        self.lidar = LidarDist()

        self.team_color_feed = Bool()

        # Initialize positions
        self.pos = Vector3()
        self.imu = Imu()
        self.orientation = 0.0
        self.target_x = 0.0
        self.target_y = 0.0
        self.y_mode = 0.0
        self.x_mode = 0.0
        self.target_heading = 0.0

        self.imu_counter = 0
        self.offset_w = 0
        self.corrected_yaw = 0.0
        
        self.get_first = True

        # Timer
        self.timer = self.create_timer(0.1, self.movement)
        # self.timer = self.create_timer(0.1, self.moving)

        self.move = True

        # Initialize PID controllers
        self.driveOutput = PID(0, 2, 0, 1, 10)
        self.turnOutput = PID(0, 2, 0, 0.08, 10)
        self.driveVx = PID(0, 40, 0.01)
        self.driveVy = PID(0, 40, 0.01)
        self.turnPID = PID(0, 5, 0.01)
        self.turnPID1 = PID(0, 50, 0.01)

    def team_color_callback(self, msg):
        self.team_color_feed = msg
        
    def lidar_dist(self, msg):
        self.lidar = msg
        if self.get_first:
            self.target_y = self.lidar.y * -1
            self.get_first = False
        if self.team_color_feed.data:
            self.lidar.y = self.lidar.y * -1

    def odometry_callback(self, msg):
        self.pos = msg
    
    def imu_callback(self, msg):
        self.imu = msg
        # if self.imu_counter == 0:
        #     self.offset_w = self.imu.orientation.w
        #     self.get_logger().info(f'self.offset_w: {self.offset_w}')
        #     self.imu_counter = 1
            
        # if self.offset_w > math.pi:
        #     if self.imu.orientation.w < math.pi:
        #         self.corrected_yaw = self.imu.orientation.w + (2*math.pi - self.offset_w)

        # if self.imu.orientation.w < math.pi:
        #     if self.offset_w > math.pi:
        #         self.corrected_yaw = self.imu.orientation.w + (2*math.pi - self.offset_w)
        #     else:
        #         self.corrected_yaw = (self.offset_w - self.imu.orientation.w) * -1
        # else:
        #     if self.offset_w > math.pi:
        #         self.corrected_yaw = (self.imu.orientation.w - self.offset_w)
        #     else: 
        #         self.corrected_yaw = (self.offset_w + (2*math.pi - self.imu.orientation.w)) * -1
        if self.imu_counter == 0:
            self.offset_w = self.imu.orientation.w
            self.get_logger().info(f'self.offset_w: {self.offset_w}')
            self.imu_counter = 1
        
        # Get the current yaw from the IMU
        current_yaw = self.imu.orientation.w
        
        # Normalize current yaw to be within [-PI, PI]
        current_yaw = (current_yaw + math.pi) % (2 * math.pi) - math.pi
        
        # Calculate corrected yaw
        self.corrected_yaw = current_yaw - self.offset_w
        
        # Normalize corrected yaw to be within [-2PI, 2PI]
        if self.corrected_yaw > math.pi:
            self.corrected_yaw -= 2 * math.pi
        elif self.corrected_yaw < -math.pi:
            self.corrected_yaw += 2 * math.pi
        
        # self.get_logger().info(f'Corrected Yaw: {self.corrected_yaw}')

    def cmd_vel_callback(self, msg):
        self.target_x = msg.linear.x
        self.target_y = msg.linear.y
        self.y_mode = msg.linear.z
        self.x_mode = msg.linear.z
        self.target_heading = msg.angular.z

    # def moving(self):
    #     targets = [100, 0, 0]
    #     self.get_logger().info(f'targets: {targets}')
    #     self.target_x = targets[0]
    #     self.target_y = targets[1]
    #     self.target_heading = targets[2]
    #     while self.move:
    #         self.get_logger().info(f'Target x {self.target_x}')
    #         self.movement()
    #         self.get_logger().info(f'Move Bool {self.move}')
    #         # self.move = False
        
    #     self.get_logger().info(f'Move complete')

    def clamp(input_value, min_value, max_value):
        if input_value > max_value:
            return max_value
        if input_value < min_value:
            return min_value
        return input_value


    def movement(self):
        print('Hello')
        turnOutput_PID = self.turnOutput.calculate_pid_output((self.target_heading) - (self.corrected_yaw))
        driveOutput_PID = self.driveOutput.calculate_pid_output(math.hypot(self.target_x - self.pos.x, self.target_y + self.lidar.y))

        turnSettled = self.turnOutput.is_settled()
        self.get_logger().info(f'error {(self.target_heading) - (self.corrected_yaw)}')
        self.get_logger().info(f'orientation {(self.corrected_yaw)}')
        self.get_logger().info(f'Offset {(self.offset_w)}')
        self.driveOutput.setpoint = math.hypot(self.target_x - self.pos.x, self.target_y + self.lidar.y)
        self.driveVx.setpoint = self.target_x - self.pos.x
        self.driveVy.setpoint = self.target_y + self.lidar.y
        self.turnPID.setpoint = (self.target_heading) - (self.corrected_yaw)
        self.turnPID1.setpoint = (self.target_heading) - (self.corrected_yaw)

        if not self.driveOutput.is_settled() or not turnSettled:
            self.get_logger().info(f'target_heading {(self.target_heading)}')
            turnSettled = self.turnOutput.is_settled()
            self.get_logger().info(f'target y {self.target_y}')
            self.get_logger().info(f'pos x {self.pos.x}')
            self.get_logger().info(f'self.lidar.y {self.lidar.y}')
            error_x = self.target_x - self.pos.x
            error_y = self.target_y + self.lidar.y 
            self.get_logger().info(f'error_y {error_y}')
            heading_error = (self.target_heading) - (self.corrected_yaw)

            theta2 = math.atan2(error_y, error_x)
            
            Vy = (math.cos(theta2) - math.sin(theta2))
            Vx = (math.sin(theta2) + math.cos(theta2))
            self.get_logger().info(f'Vx {Vx}')
            self.get_logger().info(f'Vy {Vy}')

            Vx_PID = self.driveVx.calculate_pid_output(error_x)
            Vy_PID = self.driveVy.calculate_pid_output(error_y)
            omega_PID = self.turnPID.calculate_pid_output(heading_error)
            omega_PID1 = self.turnPID1.calculate_pid_output(heading_error)
            self.get_logger().info(f'Vx_PID {Vx_PID}')
            self.get_logger().info(f'Vy_PID {Vy_PID}')
            # self.get_logger().info(f'Omega_PID {omega_PID}')


            Vx = (Vx_PID + Vx)
            Vy = (Vy_PID + Vy) 
            omega = -1 *omega_PID
            


            Vx = max(min(Vx, 3000.0), -3000.0)
            Vy = max(min(Vy, 3000.0), -3000.0)
            if self.y_mode == -1.0:
                self.get_logger().info(f'Hello world')
                Vy = 0.0
            if self.x_mode == -2.0:
                self.get_logger().info(f'Hello world')
                Vx = 0.0

            # if(Vx < 80 and Vx > 0):
            #     Vx = 80.0
            # elif(Vx > -80 and Vx < 0):
            #     Vx = -80.0
            
            # if(Vy < 80 and Vy > 0):
            #     Vy = 80.0
            # elif(Vy > -80 and Vy < 0):
            #     Vy = -80.0

            self.get_logger().info(f'Omega {omega}')
            self.get_logger().info(f'Omega_PID1 {omega_PID1}')
            # if self.target_heading == 0.0:
            #     if omega < 10 and omega > 0.08:
            #         omega = 10.0
            #     elif omega > -10 and omega < -0.08:
            #         omega = -10.0
            #     elif omega == 0:
            #         omega = 0.0
            # else:
            #     omega = -1 * omega_PID1

            if omega < 10 and omega > 0.08:
                omega = 10.0
            elif omega > -10 and omega < -0.08:
                omega = -10.0
            elif omega == 0:
                omega = 0.0


            


            if (self.target_heading) != 0 and self.target_x == 0 and self.target_y == 0:
                Vx = 0.0
                Vy = 0.0
                self.get_logger().info("Rotation")

            else:
                # turnSettled = True
                self.get_logger().info("Linear")

            velocity_command = Vector3()
            velocity_command.x = Vx
            # velocity_command.x = 0.0
            print(f'Type: {type(omega)}')
            velocity_command.y = Vy
            velocity_command.z = omega

            bool_done = WayPoint()
            error = math.hypot(self.target_x - self.pos.x, self.target_y + self.lidar.y)
            bool_done.error = error
            bool_done.done = False

            # self.get_logger().info(f'Publishing bool {bool_done.done}')


            self.velocity_publisher.publish(velocity_command)
            self.way_point_bool.publish(bool_done)

            self.get_logger().info(f'Publishing velocity: Vx={Vx}, Vy={Vy}, omega={omega}')
        elif self.driveOutput.is_settled() or turnSettled:
            self.get_logger().info("Settled")
            velocity_command = Vector3()
            # velocity_command.x = 0.0
            # velocity_command.y = 0.0
            # velocity_command.z = 0.0
            self.velocity_publisher.publish(velocity_command)

            bool_done = WayPoint()
            bool_done.done = True
            self.way_point_bool.publish(bool_done)

            self.move = False


def main(args=None):
    rclpy.init(args=args)
    node = MovementControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()