import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    simulation_dir = get_package_share_directory('Prodev_simulation')
    slam_dir = get_package_share_directory('Prodev_slam')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    simulation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(simulation_dir, 'launch', 'gazebo_sim.launch.py')
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items(),
    )

    cartographer_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(slam_dir, 'launch', 'cartographer.launch.py')
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items(),
    )

    return LaunchDescription([
        simulation_launch,
        cartographer_launch,
    ])
