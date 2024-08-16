from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Node(
        #     package='ros_imu',
        #     executable='ros_imu',
        #     name='ros_imu_node'
        # ),
        Node(
            package='my_robot',
            executable='arduino_feedback',
            name='arduino_feedback_node'
        ),
        # Node(
        #     package='get_dist',
        #     executable='get_dist',
        #     name='get_dist_node'
        # ),
        Node(
            package='movement',
            executable='smart_driver_send',
            name='smart_driver_send_node'
        ),
        Node(
            package='auto_r2',
            executable='rail_control',
            name='rail_control_node'
        )
    ])