FROM ros@sha256:6513503d0b10e919fbe8134981d4f9d19b5c1f9b045b87a9fe3b0b9e03e7c2a9

ARG DEBIAN_FRONTEND=noninteractive

# Set locale and timezone
ENV LANG=en_US.UTF-8
ENV LC_ALL=C.UTF-8
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install essential build tools and remaining ROS2/Gazebo dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    cmake \
    python3-pip \
    python3-colcon-common-extensions \
    python3-vcstool \
    python3-colcon-mixin \
    wget \
    vim \
    bash-completion \
    ros-jazzy-desktop \
    ros-jazzy-ros-gz \
    ros-jazzy-robot-state-publisher \
    ros-jazzy-joint-state-publisher \
    ros-jazzy-joint-state-publisher-gui \
    ros-jazzy-xacro \
    ros-jazzy-tf2-ros \
    ros-jazzy-tf2-tools \
    ros-jazzy-rviz2 \
    ros-jazzy-ament-* \
    && rm -rf /var/lib/apt/lists/*

# Create workspace
ENV ROS_WS=/ros2_ws
RUN mkdir -p ${ROS_WS}/src
WORKDIR ${ROS_WS}

# Copy source packages
COPY Prodev_simulation/ ${ROS_WS}/src/Prodev_simulation/
COPY Prodev_bringup/ ${ROS_WS}/src/Prodev_bringup/
COPY Prodev_slam/ ${ROS_WS}/src/Prodev_slam/

# Copy cartographer repos file and import external sources
COPY cartographer.repos ${ROS_WS}/cartographer.repos
RUN vcs import ${ROS_WS}/src < ${ROS_WS}/cartographer.repos

# Build the workspace
RUN /bin/bash -c "source /opt/ros/jazzy/setup.bash && colcon build --symlink-install"

# Create entrypoint script
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
# Source ROS2\n\
source /opt/ros/jazzy/setup.bash\n\
\n\
# Source workspace if built\n\
if [ -f ${ROS_WS}/install/setup.bash ]; then\n\
    source ${ROS_WS}/install/setup.bash\n\
fi\n\
\n\
exec "$@"' > /ros2_entrypoint.sh \
    && chmod +x /ros2_entrypoint.sh

ENTRYPOINT ["/ros2_entrypoint.sh"]
CMD ["bash"]
