# Changelog

All notable changes to this project will be documented in this file.

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

### Changed
- Restructure project layout.
- Update `Prodev_simulation` package with proper `package.xml` and `CMakeLists.txt`.
- Update `gazebo_sim.launch.py` to use `Prodev_simulation` and `Prodev_bringup` packages.
- Update README with Docker build/run instructions, mirror selection, and WSL2 notes.
- Update `.gitignore` with common ROS2/IDE/OS exclusions.

### Fixed
- Fix `gz sim` launch command by removing invalid `-f` option.
- Fix `Prodev_bringup` package by removing references to non-existent config/rviz directories.
- Adjust robot initial spawn position to avoid wall collision in `slam_maze.world`.

## [0.0.1] - 2026-06-25

### Added
- Initial project structure.
- Basic `Prodev_simulation` package with URDF, launch file, and empty Gazebo world.
- Project documentation (README, docs).