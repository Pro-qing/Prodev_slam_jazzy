#!/bin/bash
# Docker run script for Prodev SLAM Jazzy
# Usage: bash scripts/docker_run.sh [options]
#   --build    Force rebuild Docker image
#   --gui      Enable GUI support (X11 forwarding for RViz2/Gazebo)
#   --dev      Mount local source code for development
#   --mirror   Select apt mirror: official (default) or ustc
#   --wsl      Adjust X11/GPU settings for Windows WSL2

set -e

IMAGE_NAME="prodev_jazzy"
CONTAINER_NAME="prodev_jazzy_container"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Project root is the directory containing this scripts/ folder
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

BUILD=false
GUI=false
DEV=false
WSL=false
MIRROR="official"

# Parse arguments
while [[ $# -gt 0 ]]; do
    arg="$1"
    case $arg in
        --build)  BUILD=true ; shift ;;
        --gui)    GUI=true ; shift ;;
        --dev)    DEV=true ; shift ;;
        --wsl)    WSL=true ; shift ;;
        --mirror)
            if [ -n "$2" ] && [ "${2:0:1}" != "-" ]; then
                MIRROR="$2"
                shift 2
            else
                echo "Error: --mirror requires a value (official or ustc)"
                exit 1
            fi
            ;;
        --help|-h)
            echo "Usage: bash scripts/docker_run.sh [options]"
            echo ""
            echo "Options:"
            echo "  --build          Force rebuild Docker image"
            echo "  --gui            Enable GUI support (X11 forwarding for RViz2/Gazebo)"
            echo "  --dev            Mount local source code for development"
            echo "  --wsl            Adjust X11/GPU settings for Windows WSL2"
            echo "  --mirror <name>  Select apt mirror: official (default) or ustc"
            echo "  --help           Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $arg"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

if [ "$MIRROR" != "official" ] && [ "$MIRROR" != "ustc" ]; then
    echo "Error: --mirror must be 'official' or 'ustc'"
    exit 1
fi

# Build image if requested or if image does not exist
if [ "$BUILD" = true ] || [ -z "$(docker images -q ${IMAGE_NAME} 2>/dev/null)" ]; then
    echo "Building Docker image: ${IMAGE_NAME} (mirror: ${MIRROR})..."
    docker build -t ${IMAGE_NAME} --build-arg MIRROR=${MIRROR} -f ${PROJECT_ROOT}/Dockerfile ${PROJECT_ROOT}
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
        --env="QT_X11_NO_MITSHM=1"
        --env="XAUTHORITY=${XAUTHORITY:-$HOME/.Xauthority}"
        --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"
        --gpus all
        --env="NVIDIA_VISIBLE_DEVICES=all"
        --env="NVIDIA_DRIVER_CAPABILITIES=all"
    )

    if [ "$WSL" = true ]; then
        echo "WSL2 mode: configuring DISPLAY for Windows host X Server..."
        WSL_DISPLAY=$(grep -m 1 nameserver /etc/resolv.conf | awk '{print $2}'):0
        RUN_ARGS+=(--env="DISPLAY=${WSL_DISPLAY}")
    else
        RUN_ARGS+=(--env="DISPLAY=$DISPLAY")
    fi

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
