# Import necessary modules
import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Define the nodes to launch
    arduino_feedback_node = Node(
        package='my_robot',
        executable='arduino_feedback',
        name='arduino_feedback'
    )
    
    smart_driver_send_node = Node(
        package='movement',
        executable='smart_driver_send',
        name='smart_driver_send'
    )
    
    rail_control_node = Node(
        package='auto_r2',
        executable='rail_control',
        name='rail_control'
    )
    
    # Create the launch description and populate
    ld = LaunchDescription()
    
    # Add the nodes to the launch description
    ld.add_action(arduino_feedback_node)
    ld.add_action(smart_driver_send_node)
    ld.add_action(rail_control_node)
    
    return ld