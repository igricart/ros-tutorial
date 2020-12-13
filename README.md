# Python Workspace

This repository is meant to have basic concepts of ROS using python

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