# Benchmarks 性能基准

本目录用于存放项目性能基准测试记录。

## Cartographer SLAM 建图性能

### 测试环境

- **操作系统**：Ubuntu 24.04 (Noble)
- **ROS2 版本**：Jazzy Jalisco
- **仿真器**：Gazebo Sim 8.11.0
- **物理引擎**：DartSim
- **CPU**：待补充
- **GPU**：NVIDIA RTX 5070（仅用于渲染，SLAM 不依赖 GPU）
- **运行方式**：Docker 容器

### 参考指标

| 指标 | 参考值 |
|------|--------|
| LiDAR 扫描频率 | 10 Hz |
| IMU 数据频率 | 100 Hz |
| 里程计频率 | 100 Hz |
| 地图分辨率 | 0.05m |
| Cartographer 子图发布周期 | 0.3s |
| Cartographer 位姿发布周期 | 5ms |
| TF 发布频率 | ~17 Hz (DiffDrive) |

### 系统资源参考

| 资源 | Cartographer 运行时参考 |
|------|------------------------|
| CPU 占用 | 待测量 |
| 内存占用 | 待测量 |
| 地图文件大小 | ~3.0 MB (pbstream) |

### 测试方法

```bash
# 启动仿真 + SLAM
ros2 launch Prodev_slam slam_sim.launch.py

# 新终端监控资源
docker exec -it prodev_jazzy_container bash
top -p $(pgrep -d',' -f cartographer)

# 或使用 ros2 topic hz 检查话题频率
ros2 topic hz /scan
ros2 topic hz /odom
ros2 topic hz /tf
```

> 详细基准测试数据待补充。