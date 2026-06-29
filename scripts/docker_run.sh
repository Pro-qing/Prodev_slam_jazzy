#!/bin/bash
# Docker run script for Prodev SLAM Jazzy
# Usage: bash scripts/docker_run.sh [options]
#   --build    Force rebuild Docker image
#   --gui      Enable GUI support (X11 forwarding for RViz2/Gazebo)
#   --dev      Mount local source code for development

set -e

IMAGE_NAME="prodev_jazzy"
CONTAINER_NAME="prodev_jazzy_container"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Project root is the directory containing this scripts/ folder
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

BUILD=false
GUI=false
DEV=false

# Parse arguments
for arg in "$@"; do
    case $arg in
        --build)  BUILD=true ;;
        --gui)    GUI=true ;;
        --dev)    DEV=true ;;
        --help|-h)
            echo "Usage: bash scripts/docker_run.sh [options]"
            echo ""
            echo "Options:"
            echo "  --build    Force rebuild Docker image"
            echo "  --gui      Enable GUI support (X11 forwarding for RViz2/Gazebo)"
            echo "  --dev      Mount local source code for development"
            echo "  --help     Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $arg"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Build image if requested or if image does not exist
if [ "$BUILD" = true ] || [ -z "$(docker images -q ${IMAGE_NAME} 2>/dev/null)" ]; then
    echo "Building Docker image: ${IMAGE_NAME}..."
    docker build -t ${IMAGE_NAME} -f ${PROJECT_ROOT}/Dockerfile ${PROJECT_ROOT}
fi

# Stop and remove existing container with same name
if [ "$(docker ps -aq -f name=${CONTAINER_NAME})" ]; then
    echo "Removing existing container: ${CONTAINER_NAME}..."
    docker rm -f ${CONTAINER_NAME}
fi

# Build run command
RUN_ARGS=(
    -it
    --rm
    --name ${CONTAINER_NAME}
    --net=host
    --env="ROS_WS=/ros2_ws"
)

if [ "$GUI" = true ]; then
    echo "Enabling GUI support (X11 forwarding) and NVIDIA GPU (RTX 5070)..."
    xhost +local:docker 2>/dev/null || true
    RUN_ARGS+=(
        --env="DISPLAY=$DISPLAY"
        --env="QT_X11_NO_MITSHM=1"
        --env="XAUTHORITY=${XAUTHORITY:-$HOME/.Xauthority}"
        --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"
        --gpus all
        --env="NVIDIA_VISIBLE_DEVICES=all"
        --env="NVIDIA_DRIVER_CAPABILITIES=all"
    )

    # Mount DRI/GPU devices when available
    if [ -d /dev/dri ]; then
        RUN_ARGS+=(--volume="/dev/dri:/dev/dri")
    fi
fi

if [ "$DEV" = true ]; then
    echo "Development mode: mounting local source code..."
    RUN_ARGS+=(
        --volume="${PROJECT_ROOT}/Prodev_simulation:/ros2_ws/src/Prodev_simulation"
        --volume="${PROJECT_ROOT}/Prodev_bringup:/ros2_ws/src/Prodev_bringup"
    )
fi

echo "Starting container: ${CONTAINER_NAME}..."
docker run "${RUN_ARGS[@]}" ${IMAGE_NAME}
