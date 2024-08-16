from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Define the nodes

    
    # odometry_cont_node = Node(
    #     package='odometry_cont',
    #     executable='odometry_cont',  # Placeholder, replace with actual executable name
    #     name='odometry_cont'
    # )
    
    my_robot_node = Node(
        package='my_robot',
        executable='my_robot',  # Placeholder, replace with actual executable name
        name='my_robot'
    )
    
    auto_r2_node = Node(
        package='auto_r2',
        executable='auto_r2',
        name='auto_r2'
    )
    
    movement_node = Node(
        package='movement',
        executable='movement',
        name='movement'
    )
    
    # Create the launch description
    ld = LaunchDescription()
    
    # Add nodes to the launch description
    ld.add_action(my_robot_node)
    # ld.add_action(odometry_cont_node)
    ld.add_action(auto_r2_node)
    ld.add_action(movement_node)
    
    return ld