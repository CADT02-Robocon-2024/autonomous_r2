# Import necessary modules
import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Define the live_detection_node to launch
    live_detection_node = Node(
        package='my_package',  # Name of the package where the node is located
        executable='live_detection_node',  # Name of the executable to run
        name='live_detection_node',  # Optional: Rename the node
        # output='screen',  # Optional: Display the node's output in the terminal
        # Additional parameters can be added here as needed
    )

    # Create and return the LaunchDescription object
    return LaunchDescription([
        live_detection_node,  # Add the live_detection_node to the launch description
    ])