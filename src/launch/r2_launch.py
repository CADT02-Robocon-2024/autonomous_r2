from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='odometry',
            node_namespace='scripts_odom',
            node_executable='odometry',
            node_name='odometry'
        ),
        Node(
            package='ros_imu',
            node_namespace='ros_imu',
            node_executable='ros_imu',
            node_name='ros_imu'
        )
    ])