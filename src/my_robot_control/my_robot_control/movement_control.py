import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Imu
import math
# from odometry.PID import PID  # Ensure this import is correct
import customtkinter as ctk  # Assuming this is correctly installed and imported

class MovementControl(Node):

    def __init__(self):
        super().__init__('movement_control')

        # Initialize positions and variables
        self.pos = Vector3()
        self.imu = Imu()
        self.corrected_yaw = 0.0
        self.target_x = 0.0
        self.target_y = 0.0
        self.target_heading = 0.0

        # # Initialize PID controllers
        # self.driveOutput = PID(0, 2, 0, 10, 20)
        # self.turnOutput = PID(0, 2, 0, 0.03, 10)
        # self.driveVx = PID(0, 35, 0)
        # self.driveVy = PID(0, 35, 0)
        # self.turnPID = PID(0, 50, 0)

        # Initialize GUI
        self.init_gui()

        # Subscriptions
        # self.odom_sub = self.create_subscription(Vector3, 'odometry', self.odometry_callback, 10)
        # self.cmd_vel_sub = self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        # self.imu_sub = self.create_subscription(Imu, 'imu/data_raw', self.imu_callback, 10)

        # Publisher
        self.velocity_publisher = self.create_publisher(Vector3, 'velocity_command', 10)

        # Timer
        self.timer = self.create_timer(0.1, self.movement)

    def init_gui(self):
        self.app = ctk.CTk()
        self.app.title("CADT 02 ABU Robocon GUI")
        self.app.geometry("1000x600")

        # Set appearance mode to dark
        ctk.set_appearance_mode("dark")

        # Configure main window's grid to be responsive
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_columnconfigure(1, weight=3)

        # Create sidebar frame
        self.sidebar_frame = ctk.CTkFrame(self.app, width=200, corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        # Create main content frame
        self.main_frame = ctk.CTkFrame(self.app, corner_radius=10)
        self.main_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Add buttons to the sidebar
        self.home_button = ctk.Button(self.sidebar_frame, text="Home", command=self.show_home)
        self.home_button.grid(row=0, column=0, pady=10, padx=10)

        self.testing_button = ctk.Button(self.sidebar_frame, text="Testing", command=self.show_testing)
        self.testing_button.grid(row=1, column=0, pady=10, padx=10)

        self.test_ii_button = ctk.Button(self.sidebar_frame, text="Test II", command=self.show_test_ii)
        self.test_ii_button.grid(row=2, column=0, pady=10, padx=10)

        # Run the main loop
        self.app.mainloop()

    def odometry_callback(self, msg):
        self.pos = msg

    def imu_callback(self, msg):
        self.imu = msg
        # Implement your IMU callback logic here

    def cmd_vel_callback(self, msg):
        self.target_x = msg.linear.x
        self.target_y = msg.linear.y
        self.target_heading = msg.angular.z

    def movement(self):
        turnOutput_PID = self.turnOutput.calculate_pid_output(self.target_heading - self.corrected_yaw)
        driveOutput_PID = self.driveOutput.calculate_pid_output(math.hypot(self.target_x - self.pos.x, self.target_y - self.pos.y))

        # Implement your movement control logic here

    def show_home(self):
        # Implement the logic for displaying the "Home" view in GUI
        pass

    def show_testing(self):
        # Implement the logic for displaying the "Testing" view in GUI
        pass

    def show_test_ii(self):
        # Implement the logic for displaying the "Test II" view in GUI
        pass

if __name__ == '__main__':
    rclpy.init()
    node = MovementControl()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()
