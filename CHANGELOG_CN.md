# 更新日志

本项目的所有重要变更都将记录在此文件中。

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

### 变更
- 调整项目目录结构。
- 完善 `Prodev_simulation` 功能包的 `package.xml` 和 `CMakeLists.txt`。
- 更新 `gazebo_sim.launch.py`，使用 `Prodev_simulation` 和 `Prodev_bringup` 功能包。
- 更新 README，添加 Docker 构建/运行说明、镜像源选择和 WSL2 注意事项。
- 更新 `.gitignore`，添加常见的 ROS2/IDE/系统文件忽略规则。

### 修复
- 修复 `gz sim` 启动命令，移除无效的 `-f` 参数。
- 修复 `Prodev_bringup` 功能包，移除不存在的 config/rviz 目录引用。
- 调整机器人在 `slam_maze.world` 中的初始生成位置，避免与墙壁干涉。

## [0.0.1] - 2026-06-25

### 新增
- 初始项目结构。
- 基础的 `Prodev_simulation` 功能包，包含 URDF、启动文件和空 Gazebo 世界。
- 项目文档（README、docs）。