# Demo 演示

本目录用于存放项目演示内容。

## Cartographer SLAM 建图演示

### 演示环境

- Ubuntu 24.04 + ROS2 Jazzy + Gazebo Sim 8
- Docker 容器运行（镜像：`prodev_jazzy`）
- 迷宫世界：`slam_maze.world`

### 演示步骤

1. **构建并启动容器**
   ```bash
   bash scripts/docker_run.sh --no-cache --gui --mirror ustc
   ```

2. **启动仿真 + SLAM**
   ```bash
   source /ros2_ws/install/setup.bash
   ros2 launch Prodev_slam slam_sim.launch.py
   ```

3. **键盘控制机器人建图**
   ```bash
   # 新终端进入容器
   docker exec -it prodev_jazzy_container bash
   ros2 run teleop_twist_keyboard teleop_twist_keyboard
   ```

4. **操作方式**
   - `i` 前进 / `,` 后退 / `j` 左转 / `l` 右转 / `k` 停止

5. **保存地图**
   ```bash
   ros2 service call /finish_trajectory cartographer_ros_msgs/srv/FinishTrajectory "{trajectory_id: 0}"
   ros2 service call /write_state cartographer_ros_msgs/srv/WriteState "{filename: '/ros2_ws/map.pbstream'}"
   ```

### 预期效果

- rviz2 中显示机器人模型、激光扫描点、TF 坐标系
- 机器人移动后，Map 显示项逐渐构建出迷宫地图
- Cartographer 节点持续运行，不崩溃
- 最终可保存完整的迷宫地图文件

### 已保存示例地图

`Prodev_slam/maps/map.pbstream` — 在 `slam_maze.world` 迷宫中建图的 Cartographer pbstream 格式地图。