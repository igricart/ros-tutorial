cmake_minimum_required(VERSION 3.5)

project(behavior_tree)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
find_package(catkin REQUIRED
  COMPONENTS roscpp behaviortree_cpp_v3 
)

catkin_package(
    CATKIN_DEPENDS roscpp behaviortree_cpp_v3
)

include_directories(include ${catkin_INCLUDE_DIRS})
add_executable(${PROJECT_NAME} "src/hello_BT.cpp")
target_link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES})
