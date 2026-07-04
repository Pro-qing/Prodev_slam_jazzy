# Changelog

All notable changes to this project will be documented in this file.

## [0.0.3] - 2026-07-05

### Added
- Add `Prodev_slam` SLAM package with Cartographer 2D mapping algorithm integration.
- Add `cartographer.launch.py` launch file with automatic Cartographer node and rviz2 visualization.
- Add `slam_sim.launch.py` integrated simulation + SLAM launch file.
- Add `cartographer_2d.lua` Cartographer 2D mapping parameter configuration.
- Add `rviz/cartographer.rviz` SLAM visualization configuration (Map, LaserScan, RobotModel, TF).
- Add `Prodev_slam/maps/map.pbstream` saved Cartographer map file.
- Add rear caster wheel to robot model for improved stability.
- Add complete SLAM mapping workflow documentation (keyboard control, map saving) to README.
- Add robot model description and sensor configuration to README.
- Add NVIDIA Container Toolkit prerequisite documentation to README.
- Add `--no-cache` independent option to `docker_run.sh` for rebuilding without Docker cache.
- Use binary `ros-jazzy-cartographer-ros` and `ros-jazzy-cartographer-rviz` packages instead of building from source.
- Update `Prodev_slam/CMakeLists.txt` install rules to include `maps` directory.

### Changed
- Update README map saving section to use Cartographer services instead of nav2_map_server.
- Configure DiffDrive plugin `odom_frame_id` and `child_frame_id` to remove Gazebo `robot/` prefix issue.
- Restore ros_gz_bridge TF bridge (`/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V`).
- Restore Cartographer config `provide_odom_frame = false` and `published_frame = "odom"`.
- Update `cartographer.launch.py` to auto-start rviz2 visualization.
- Update Dockerfile with Cartographer dependencies.
- Unify all package versions to `0.0.3`.

### Fixed
- Fix DiffDrive plugin missing TF bridge: add `<tf_topic>/tf</tf_topic>` to publish `odom → base_link` TF to ROS.
- Fix IMU frame offset: change `imu_joint` origin to `xyz="0 0 0"` to colocate IMU frame with `base_link`.
- Fix rviz Map display QoS Durability Policy from Volatile to Transient Local, resolving map not displaying.
- Fix rviz config missing Interact tool and RobotModel display.
- Fix `rviz/cartographer.rviz` Panel class names to use correct ROS2 Jazzy classes.
- Fix robot drive wheel axis direction to correct forward movement.

## [0.0.2] - 2026-06-30

### Added
- Add production `Dockerfile` at repository root for building standalone Docker image.
- Add `scripts/docker_run.sh` with options: `--build`, `--gui`, `--dev`, `--mirror`, `--wsl`.
- Support optional USTC apt mirror via `--build-arg MIRROR=ustc` for faster builds in China.
- Add VS Code Dev Container configuration (`.devcontainer/`).
- Add `Prodev_bringup` package as top-level system bringup entry.
- Add `slam_maze.world` Gazebo world for SLAM simulation.
- Support selecting Gazebo world file via `world` launch argument.
- Add `sensor_tf.launch.py` for static sensor calibration TF publishers.
- Add GitHub issue and pull request templates.
- Add `CONTRIBUTING.md` contribution guidelines.
- Add `LICENSE` under GNU General Public License v3.0 (GPL-3.0).
- Expand `slam_maze.world` with new outer boundary and internal elements.
- Add internal zig-zag partition walls to extended maze region.

### Changed
- Restructure project layout.
- Update `Prodev_simulation` package with proper `package.xml` and `CMakeLists.txt`.
- Update `gazebo_sim.launch.py` to use `Prodev_simulation` and `Prodev_bringup` packages.
- Update README with Docker build/run instructions, mirror selection, and WSL2 notes.
- Update `.gitignore` with common ROS2/IDE/OS exclusions.
- Refactor `Prodev_simulation` package to be self-contained.

### Fixed
- Fix `gz sim` launch command by removing invalid `-f` option.
- Fix `Prodev_bringup` package by removing references to non-existent config/rviz directories.
- Adjust robot initial spawn position to avoid wall collision in `slam_maze.world`.
- Adjust poses and dimensions for new inner walls in extended maze region.

## [0.0.1] - 2026-06-25

### Added
- Initial project structure.
- Basic `Prodev_simulation` package with URDF, launch file, and empty Gazebo world.
- Project documentation (README, docs).