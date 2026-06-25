# Prodev SLAM Jazzy

基于 ROS2 Jazzy 的 SLAM 仿真项目，使用 Ubuntu 24.04 和 Gazebo 进行机器人仿真。

## 项目结构

```
Prodev_slam_jazzy/
├── Prodev_simulation/       # 仿真功能包
│   ├── config/              # 配置文件 (TF 参数等)
│   ├── launch/              # Launch 启动文件
│   ├── urdf/                # 机器人 URDF 模型
│   └── worlds/              # Gazebo 世界文件
├── docs/                    # 项目文档
├── scripts/                 # 脚本工具
├── tools/                   # 工具
└── demo/                    # 演示
```

## 环境要求

- **操作系统**: Ubuntu 24.04 (Noble)
- **ROS2 版本**: Jazzy Jalisco
- **仿真器**: Gazebo
- **构建工具**: colcon

## Docker 部署

### 构建镜像

在项目根目录执行：

```bash
docker build -t prodev_jazzy .
```

### 运行容器

**基本运行：**

```bash
docker run -it --name prodev_jazzy_container prodev_jazzy
```

**支持 GUI 显示（RViz2 / Gazebo）：**

```bash
# 允许 Docker 访问 X11 显示
xhost +local:docker

docker run -it --name prodev_jazzy_container \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    prodev_jazzy
```

**挂载本地代码（开发模式）：**

```bash
docker run -it --name prodev_jazzy_container \
    --volume="$(pwd)/src:/ros2_ws/src" \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    prodev_jazzy
```

### 便捷脚本

使用 `scripts/docker_run.sh` 快速启动：

```bash
bash scripts/docker_run.sh
```

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

# 启动 Gazebo 仿真
ros2 launch Prodev_simulation gazebo_sim.launch.py
```

## License

详见 [LICENSE](./LICENSE)