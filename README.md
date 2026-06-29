# Prodev SLAM Jazzy

基于 ROS2 Jazzy 的 SLAM 仿真项目，使用 Ubuntu 24.04 和 Gazebo Sim (gz sim) 进行机器人仿真。

## 项目结构

```
Prodev_slam_jazzy/
├── Prodev_bringup/          # 顶层系统启动功能包
│   ├── config/              # 系统配置文件
│   ├── launch/              # 顶层 launch 文件
│   └── rviz/                # RViz 配置文件
├── Prodev_simulation/       # 仿真功能包
│   ├── config/              # 配置文件 (TF 参数等)
│   ├── launch/              # Launch 启动文件
│   ├── urdf/                # 机器人 URDF 模型
│   └── worlds/              # Gazebo 世界文件
├── .devcontainer/           # VS Code Dev Container 配置
├── docs/                    # 项目文档
├── scripts/                 # 脚本工具
├── tools/                   # 工具
└── demo/                    # 演示
```

## 环境要求

- **操作系统**: Ubuntu 24.04 (Noble)
- **ROS2 版本**: Jazzy Jalisco
- **仿真器**: Gazebo Sim (gz sim)
- **构建工具**: colcon

## Docker 部署

项目提供两种 Docker 使用方式：

1. **本地生产镜像**：仓库外层的 `Dockerfile`（以 `~/Prodev_jazzy` 为构建上下文），用于构建可独立运行的镜像。
2. **Dev Container**：`.devcontainer/Dockerfile`，用于 VS Code 开发容器，挂载本地源码进行开发。

### 构建本地镜像

在仓库外层目录（包含 `src/Prodev_slam_jazzy`）执行：

```bash
docker build -t prodev_jazzy .
```

### 运行容器

**基本运行：**

```bash
docker run -it --rm --name prodev_jazzy_container prodev_jazzy
```

**支持 GUI 显示（RViz2 / Gazebo）：**

```bash
# 允许 Docker 访问 X11 显示
xhost +local:docker

docker run -it --rm --name prodev_jazzy_container \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --gpus all \
    prodev_jazzy
```

**挂载本地代码（开发模式）：**

```bash
docker run -it --rm --name prodev_jazzy_container \
    --volume="$(pwd)/src/Prodev_slam_jazzy/Prodev_simulation:/ros2_ws/src/Prodev_simulation" \
    --volume="$(pwd)/src/Prodev_slam_jazzy/Prodev_bringup:/ros2_ws/src/Prodev_bringup" \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --gpus all \
    prodev_jazzy
```

### 便捷脚本

使用 `scripts/docker_run.sh` 快速启动：

```bash
# 基本运行
bash src/Prodev_slam_jazzy/scripts/docker_run.sh

# 启用 GUI（RViz2 / Gazebo），自动挂载 NVIDIA GPU
bash src/Prodev_slam_jazzy/scripts/docker_run.sh --gui

# 开发模式（挂载本地源码）
bash src/Prodev_slam_jazzy/scripts/docker_run.sh --gui --dev

# 强制重新构建镜像
bash src/Prodev_slam_jazzy/scripts/docker_run.sh --build --gui

# 使用中科大镜像源构建（适合国内网络）
bash src/Prodev_slam_jazzy/scripts/docker_run.sh --build --mirror ustc

# WSL2 下启用 GUI
bash src/Prodev_slam_jazzy/scripts/docker_run.sh --gui --wsl
```

**参数说明：**

- `--build`：强制重新构建 Docker 镜像
- `--gui`：启用 X11 转发，支持 RViz2 / Gazebo 显示
- `--dev`：挂载本地 `Prodev_simulation` 和 `Prodev_bringup` 源码
- `--mirror <official|ustc>`：选择 apt 镜像源，默认 `official`
- `--wsl`：针对 Windows WSL2 调整 X11 和 GPU 参数

> **WSL2 使用 GUI 注意**：Windows 宿主机需要运行 X Server（如 VcXsrv、Xming），并开启 "Disable access control"。

### 常用 Docker 命令

```bash
# 查看运行中的容器
docker ps

# 进入已运行的容器
docker exec -it prodev_jazzy_container bash

# 停止容器
docker stop prodev_jazzy_container

# 删除容器
docker rm prodev_jazzy_container

# 重新构建镜像（代码有变更时）
docker build --no-cache -t prodev_jazzy .
```

## 启动仿真

进入容器后：

```bash
# Source 工作空间
source /ros2_ws/install/setup.bash

# 启动 Gazebo 仿真（仿真包）
ros2 launch Prodev_simulation gazebo_sim.launch.py

# 或启动整体系统 bringup（顶层入口）
ros2 launch Prodev_bringup prodev_bringup.launch.py
```

## Dev Container

使用 VS Code 打开本项目，选择 "Reopen in Container"，即可在预配置好的容器中进行开发。容器会自动挂载 `Prodev_slam_jazzy` 到 `/ros2_ws/src/Prodev_slam_jazzy` 并执行 `colcon build`。

## License

详见 [LICENSE](./LICENSE)
