import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    SetEnvironmentVariable,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    nav2_params_file = os.path.join(
        get_package_share_directory('Prodev_nav2'),
        'config',
        'nav2_params.yaml',
    )
    nav2_map_file = LaunchConfiguration('map')
    use_sim_time = LaunchConfiguration('use_sim_time')

    return LaunchDescription([
        # Environment variable for behavior tree log level
        SetEnvironmentVariable('RCUTILS_LOGGING_BUFFERED_STREAM', '1'),

        DeclareLaunchArgument(
            'map',
            default_value=os.path.join(
                get_package_share_directory('Prodev_nav2'),
                'maps',
                'slam_maze.yaml',
            ),
            description='Full path to map yaml file',
        ),

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true',
        ),

        DeclareLaunchArgument(
            'params_file',
            default_value=nav2_params_file,
            description='Full path to the Nav2 parameters file',
        ),

        # Include Nav2 bringup launch
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')
            ),
            launch_arguments={
                'map': nav2_map_file,
                'use_sim_time': use_sim_time,
                'params_file': nav2_params_file,
            }.items(),
        ),
    ])