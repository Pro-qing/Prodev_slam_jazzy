import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    ExecuteProcess,
    TimerAction,
)
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # 获取功能包路径
    simulation_dir = get_package_share_directory('Prodev_simulation')

    # 声明参数
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    world_name = LaunchConfiguration('world', default='slam_maze')
    world_file = PathJoinSubstitution([
        FindPackageShare('Prodev_simulation'),
        'worlds',
        world_name,
    ])
    world_file_with_ext = [world_file, '.world']
    urdf_file = os.path.join(simulation_dir, 'urdf', 'robot.urdf')

    # 读取 URDF 文件内容
    with open(urdf_file, 'r') as infp:
        robot_description = infp.read()

    # 启动 Gazebo Sim (gz sim)，加载世界文件
    # -r 表示自动开始运行, -v 4 表示 verbose level 4
    gz_sim_cmd = ExecuteProcess(
        cmd=[
            'gz', 'sim',
            world_file_with_ext,
            '-r', '-v', '4',
        ],
        output='screen',
    )

    # 启动 robot_state_publisher (仿真模式)
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time,
            'robot_description': robot_description,
        }]
    )

    # 启动 joint_state_publisher (发布轮子关节状态)
    # Gz Sim 的 DiffDrive 插件不发布 /joint_states,
    # 需要此节点使 robot_state_publisher 计算轮子 TF
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time,
            'source_list': ['joint_states'],
            'rate': 50,
        }]
    )

    # 在 Gazebo 中生成机器人模型
    # 使用 ros_gz_sim 的 create 命令
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic', 'robot_description',
            '-name', 'robot',
            '-x', '0.0',
            '-y', '0.5',
            '-z', '0.5',
        ],
        output='screen',
    )

    # 启动 sensor_tf launch 文件 (传感器标定 TF)
    # Prodev_bringup 的 sensor_tf 与 URDF 中的固定关节 TF 重复，
    # 为保持 simulation 包独立，不再依赖 bringup。
    # bringup_dir = get_package_share_directory('Prodev_bringup')
    # sensor_tf_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         os.path.join(bringup_dir, 'launch', 'sensor_tf.launch.py')
    #     ),
    #     launch_arguments={
    #         'use_sim_time': use_sim_time,
    #     }.items()
    # )

    # ROS-Gazebo 桥接 (将 Gazebo 原生话题桥接到 ROS)
    # Gz Sim 传感器话题必须使用完整路径
    # 差速驱动里程计: Gazebo 默认发布到 /model/robot/odometry
    # 相机: Gazebo 发布到 /camera (image) 和 /camera_info (camera_info)
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
            '/camera@sensor_msgs/msg/Image[gz.msgs.Image',
            '/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo',
            '/imu@sensor_msgs/msg/Imu[gz.msgs.IMU',
            '/model/robot/odometry@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',
            '--ros-args',
            '--remap', '/model/robot/odometry:=/odom',
            '--remap', '/camera:=/camera/image',
            '--remap', '/camera_info:=/camera/camera_info',
        ],
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
    )

    return LaunchDescription([
        # 声明 launch 参数
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'
        ),
        DeclareLaunchArgument(
            'world',
            default_value='slam_maze',
            description='Gazebo world file name (without .world extension)'
        ),

        # 启动 Gazebo Sim
        gz_sim_cmd,

        # 启动 robot_state_publisher
        robot_state_publisher_node,

        # 启动 joint_state_publisher
        joint_state_publisher_node,

        # 延迟生成机器人 (等待 robot_state_publisher 和 Gazebo 就绪)
        TimerAction(
            period=3.0,
            actions=[spawn_entity],
        ),

        # 启动 ROS-Gazebo 桥接
        TimerAction(
            period=4.0,
            actions=[bridge],
        ),

        # # 启动传感器 TF (已由 URDF + robot_state_publisher 提供)
        # sensor_tf_launch,
    ])