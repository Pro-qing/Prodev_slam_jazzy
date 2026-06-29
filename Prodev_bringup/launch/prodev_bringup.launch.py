import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    bringup_dir = get_package_share_directory('Prodev_bringup')
    simulation_dir = get_package_share_directory('Prodev_simulation')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    # Start simulation (Gazebo + robot + sensors)
    simulation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(simulation_dir, 'launch', 'gazebo_sim.launch.py')
        ),
        launch_arguments={
            'use_sim_time': use_sim_time,
        }.items()
    )

    # TODO: add SLAM, navigation, sensor_tf and other subsystem launches here

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation clock if true'
        ),
        simulation_launch,
    ])
