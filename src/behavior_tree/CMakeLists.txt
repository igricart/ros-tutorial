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