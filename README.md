# Python Workspace

This repository is meant to have basic concepts of ROS using python / C++.

# Behavior Tree
Using [this](https://github.com/BehaviorTree/BehaviorTree.CPP) library for BehaviorTree.

One could copy the .so files and use then in the `CMakeLists.txt` file like this
```
cmake_minimum_required(VERSION 3.5)

project(behavior_tree)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
list(APPEND CMAKE_PREFIX_PATH .)
# set(CMAKE_PREFIX_PATH ./lib/)
find_package(BehaviorTreeV3)
find_package(catkin REQUIRED)

catkin_package()
include_directories(include ${catkin_INCLUDE_DIRS})
add_executable(${PROJECT_NAME} "src/hello_BT.cpp")
target_link_libraries(${PROJECT_NAME} BT::behaviortree_cpp_v3)
```

But that requires all headers included in here

# ROS

## Topics

The easiest interaction between nodes occurs via publish/subscription. We define that the message is a velocity, because in another stage this information will be used to control the robot. 

# Gazebo Integration

Following [this](http://gazebosim.org/tutorials?tut=ros_depth_camera&cat=connect_ros) tutorial, one can add a `depth camera` to simulation and visualize it in both Gazebo and RViz.

It is still necessary to start simulation with the whole setup ready.

Copying content for an [RRBot](http://gazebosim.org/tutorials?tut=ros_control&cat=connect_ros) control, some plugins are necessary in the *xacro* file

To have the simulation for _Turtlebot_ it is necessary to run

`sudo apt install ros-melodic-turtlebot3_description`

So the xacro and other files are already in the system

# Issues
When using VS Code with the ROS extension, one should be aware of an open issue related to the [intellisense feature](https://stackoverflow.com/questions/62383272/vscode-setup-with-ros-and-auto-complete). 