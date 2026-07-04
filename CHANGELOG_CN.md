# 更新日志

本项目的所有重要变更都将记录在此文件中。

## [0.0.3] - 2026-07-05

### 新增
- 添加 `Prodev_slam` SLAM 功能包，集成 Cartographer 2D 建图算法。
- 添加 `cartographer.launch.py` 启动文件，自动加载 Cartographer 节点和 rviz2 可视化。
- 添加 `slam_sim.launch.py` 仿真 SLAM 一体化启动文件。
- 添加 `cartographer_2d.lua` Cartographer 2D 建图参数配置。
- 添加 `rviz/cartographer.rviz` SLAM 可视化配置文件（Map、LaserScan、RobotModel、TF）。
- 添加 `Prodev_slam/maps/map.pbstream` 已保存的 Cartographer 地图文件。
- 添加后万向轮（rear caster）到机器人模型，提升运动稳定性。
- 添加 SLAM 建图完整流程说明（键盘控制、地图保存）到 README。
- 添加机器人模型描述和传感器配置说明到 README。
- 添加 NVIDIA Container Toolkit 环境要求说明到 README。
- `docker_run.sh` 添加 `--no-cache` 独立参数，源码有变更时强制无缓存构建。
- 使用二进制 `ros-jazzy-cartographer-ros` 和 `ros-jazzy-cartographer-rviz` 包，替代源码编译。
- 更新 `Prodev_slam/CMakeLists.txt` 安装规则，包含 `maps` 目录。

### 变更
- 更新 README 保存地图部分，使用 Cartographer 服务替代 nav2_map_server。
- 配置 DiffDrive 插件 `odom_frame_id` 和 `child_frame_id`，消除 Gazebo `robot/` 前缀问题。
- 恢复 ros_gz_bridge TF 桥接（`/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V`）。
- 恢复 Cartographer 配置 `provide_odom_frame = false` 和 `published_frame = "odom"`。
- 更新 `cartographer.launch.py` 自动启动 rviz2 可视化。
- 更新 Dockerfile，添加 Cartographer 相关依赖。
- 统一所有功能包版本号为 `0.0.3`。

### 修复
- 修复 DiffDrive 插件缺少 TF 桥接：添加 `<tf_topic>/tf</tf_topic>`，使 `odom → base_link` TF 发布到 ROS。
- 修复 IMU 帧偏移问题：`imu_joint` origin 改为 `xyz="0 0 0"`，使 IMU 帧与 `base_link` 位置重合。
- 修复 rviz Map 显示项 QoS Durability Policy 从 Volatile 改为 Transient Local，解决地图不显示问题。
- 修复 rviz 配置缺少 Interact 工具和 RobotModel 显示项。
- 修复 `rviz/cartographer.rviz` 中 Panel 类名错误，使用正确的 ROS2 Jazzy 类名。
- 修复机器人驱动轮轴方向，纠正前进方向。

## [0.0.2] - 2026-06-30

### 新增
- 在仓库根目录添加生产环境 `Dockerfile`，用于构建独立运行的 Docker 镜像。
- 添加 `scripts/docker_run.sh` 脚本，支持 `--build`、`--gui`、`--dev`、`--mirror`、`--wsl` 选项。
- 支持通过 `--build-arg MIRROR=ustc` 使用中国科学技术大学 apt 镜像源，加速国内构建。
- 添加 VS Code Dev Container 开发容器配置（`.devcontainer/`）。
- 添加 `Prodev_bringup` 顶层系统启动功能包。
- 添加用于 SLAM 仿真的 `slam_maze.world` 迷宫地图。
- 支持通过 `world` 启动参数选择 Gazebo 世界文件。
- 添加 `sensor_tf.launch.py` 用于传感器静态标定 TF 发布。
- 添加 GitHub Issue 和 Pull Request 模板。
- 添加 `CONTRIBUTING.md` 贡献指南。
- 添加 `LICENSE`，采用 GNU General Public License v3.0 (GPL-3.0) 开源协议。
- 扩展 `slam_maze.world` 迷宫地图，添加新的外部边界和内部结构元素。
- 在扩展迷宫区域添加内部 Z 字形隔墙。

### 变更
- 调整项目目录结构。
- 完善 `Prodev_simulation` 功能包的 `package.xml` 和 `CMakeLists.txt`。
- 更新 `gazebo_sim.launch.py`，使用 `Prodev_simulation` 和 `Prodev_bringup` 功能包。
- 更新 README，添加 Docker 构建/运行说明、镜像源选择和 WSL2 注意事项。
- 更新 `.gitignore`，添加常见的 ROS2/IDE/系统文件忽略规则。
- 重构 `Prodev_simulation` 功能包，使其成为自包含的功能包。

### 修复
- 修复 `gz sim` 启动命令，移除无效的 `-f` 参数。
- 修复 `Prodev_bringup` 功能包，移除不存在的 config/rviz 目录引用。
- 调整机器人在 `slam_maze.world` 中的初始生成位置，避免与墙壁干涉。
- 调整扩展迷宫区域新内墙的位姿和尺寸，避免碰撞问题。

## [0.0.1] - 2026-06-25

### 新增
- 初始项目结构。
- 基础的 `Prodev_simulation` 功能包，包含 URDF、启动文件和空 Gazebo 世界。
- 项目文档（README、docs）。