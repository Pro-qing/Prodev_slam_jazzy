# Scripts

本目录包含项目常用脚本。

## docker_run.sh

Docker 容器快速启动脚本。

### 用法

```bash
bash scripts/docker_run.sh [options]
```

### 选项

| 选项 | 说明 |
|------|------|
| `--build` | 强制重新构建 Docker 镜像 |
| `--no-cache` | 无缓存重新构建（源码有变更时使用，隐含 `--build`） |
| `--gui` | 启用 GUI 支持（X11 转发），自动挂载 NVIDIA GPU（RTX 5070） |
| `--dev` | 挂载本地源码到容器（开发模式），包含 `Prodev_simulation`、`Prodev_bringup`、`Prodev_slam` |
| `--mirror <official\|ustc>` | 选择 apt 镜像源，默认 `official`。国内用户推荐使用 `ustc`（中科大） |
| `--wsl` | 针对 Windows WSL2 环境调整 X11 和 GPU 参数 |
| `--help` / `-h` | 显示帮助信息 |

### 示例

```bash
# 基本运行
bash scripts/docker_run.sh

# 启用 GUI（Gazebo / RViz2）
bash scripts/docker_run.sh --gui

# 开发模式：挂载本地代码并启用 GUI
bash scripts/docker_run.sh --gui --dev

# 强制重新构建镜像
bash scripts/docker_run.sh --build --gui

# 使用中科大镜像源构建（适合国内网络）
bash scripts/docker_run.sh --build --mirror ustc

# 无缓存构建（源码有变更时使用）
bash scripts/docker_run.sh --no-cache --gui --mirror ustc

# WSL2 下启用 GUI
bash scripts/docker_run.sh --gui --wsl

# 完整开发模式（构建 + GUI + 国内镜像 + 开发挂载）
bash scripts/docker_run.sh --build --gui --dev --mirror ustc
```

## 注意事项

- 使用 `--gui` 前请确保主机已安装 NVIDIA 驱动和 NVIDIA Container Toolkit。
- 若 X11 转发失败，可尝试先执行 `xhost +local:docker`。
- WSL2 用户需要在 Windows 宿主机运行 X Server（如 VcXsrv、Xming），并开启 "Disable access control"。
- 国内网络环境下建议使用 `--mirror ustc` 加速镜像构建。
