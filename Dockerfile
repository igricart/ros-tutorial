FROM ros:melodic

RUN apt update && apt install -y \
    python-catkin-tools