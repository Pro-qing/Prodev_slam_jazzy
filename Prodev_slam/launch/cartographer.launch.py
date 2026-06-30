import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    slam_dir = get_package_share_directory('Prodev_slam')
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    configuration_basename = LaunchConfiguration('configuration_basename', default='cartographer_2d.lua')

    cartographer_config_dir = os.path.join(slam_dir, 'config')

    cartographer_node = Node(
        package='cartographer_ros',
        executable='cartographer_node',
        name='cartographer_node',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=[
            '-configuration_directory', cartographer_config_dir,
            '-configuration_basename', configuration_basename,
        ],
        remappings=[
            ('scan', '/scan'),
            ('odom', '/odom'),
            ('imu', '/imu'),
        ],
    )

    cartographer_occupancy_grid_node = Node(
        package='cartographer_ros',
        executable='cartographer_occupancy_grid_node',
        name='cartographer_occupancy_grid_node',
        output='screen',
        parameters=[
            {'use_sim_time': use_sim_time},
            {'resolution': 0.05},
        ],
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation clock if true',
        ),
        DeclareLaunchArgument(
            'configuration_basename',
            default_value='cartographer_2d.lua',
            description='Name of the Cartographer configuration file',
        ),
        cartographer_node,
        cartographer_occupancy_grid_node,
    ])
