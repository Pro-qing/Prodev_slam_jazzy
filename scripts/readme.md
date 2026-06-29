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
| `--gui` | 启用 GUI 支持（X11 转发），自动挂载 NVIDIA GPU（RTX 5070） |
| `--dev` | 挂载本地源码到容器（开发模式） |
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
```

## 注意事项

- 使用 `--gui` 前请确保主机已安装 NVIDIA 驱动和 NVIDIA Container Toolkit。
- 若 X11 转发失败，可尝试先执行 `xhost +local:docker`。
