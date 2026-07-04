# Changelog

All notable changes to this project will be documented in this file.

## [0.0.3] - 2026-07-04

### Added
- Add `Prodev_nav2` Navigation2 package with configuration, launch files, and maps directory.
- Integrate Nav2 source code (`navigation2` Jazzy branch) into the project for learning and customization.
- Add `Prodev_slam` SLAM package with Cartographer algorithm integration.
- Add `cartographer.launch.py` and `slam_sim.launch.py` launch files.
- Add `cartographer_2d.lua` Cartographer 2D mapping parameter configuration.
- Add full Nav2 compilation dependencies to Dockerfile (`geographic_msgs`, `bond`, `cv_bridge`, `rviz`, `behaviortree_cpp`, etc.).
- Add `Prodev_slam` and `Prodev_nav2/navigation2` volume mounts in `docker_run.sh` dev mode.
- Add `navigation.launch.py` Nav2 navigation launch file.
- Add `nav2_params.yaml` Nav2 parameter configuration (AMCL, NavFn planner, RPP controller, etc.).

### Changed
- Update README project structure with `Prodev_slam` and `Prodev_nav2` directories.
- Update Dockerfile to compile Nav2 from local source instead of downloading at build time.

### Fixed
- Fix robot forward direction reversal by changing wheel rotation axis from `0 0 1` to `0 0 -1`.

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