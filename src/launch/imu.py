# Import necessary modules
import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Define the ros_imu node to launch
    ros_imu_node = Node(
        package='ros_imu',  # Name of the package where the node is located
        executable='ros_imu',  # Name of the executable to run
        name='ros_imu_node',  # Optional: Rename the node
        output='screen',  # Optional: Display the node's output in the terminal
        # Additional parameters can be added here as needed
    )

    # Create and return the LaunchDescription object
    return LaunchDescription([
        ros_imu_node,  # Add the ros_imu_node to the launch description
    ])