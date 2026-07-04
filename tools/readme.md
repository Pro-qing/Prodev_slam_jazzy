# Tools 工具

本目录用于存放项目辅助工具和脚本。

## 可用工具

### Docker 工具
- `scripts/docker_run.sh` — Docker 容器快速启动脚本（详见 `scripts/readme.md`）

### SLAM 工具

#### 地图保存
```bash
# 冻结 Cartographer 轨迹
ros2 service call /finish_trajectory cartographer_ros_msgs/srv/FinishTrajectory "{trajectory_id: 0}"

# 保存为 pbstream 格式
ros2 service call /write_state cartographer_ros_msgs/srv/WriteState "{filename: '/ros2_ws/map.pbstream'}"

# 从容器复制到主机
docker cp prodev_jazzy_container:/ros2_ws/map.pbstream ~/map.pbstream
```

#### 键盘控制
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

#### TF 调试
```bash
# 查看 TF 树
ros2 run tf2_tools view_frames

# 监听两个坐标系之间的 TF
ros2 run tf2_ros tf2_echo odom base_link

# 查看话题列表
ros2 topic list

# 查看话题频率
ros2 topic hz /scan
ros2 topic hz /odom
```

#### 节点诊断
```bash
# 查看运行中的节点
ros2 node list

# 查看节点信息
ros2 node info /cartographer_node

# 查看日志
ros2 topic echo /rosout --field name --field msg 2>&1 | grep -i cartographer
```

### 构建工具
```bash
# colcon 构建
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install

# 构建单个包
colcon build --packages-select Prodev_slam