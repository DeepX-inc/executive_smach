cmake_minimum_required(VERSION 3.5)
project(smach_ros
  DESCRIPTION "Extensions for the SMACH library to integrate it tightly with ROS."
)

find_package(hydra_cpack REQUIRED)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(smach REQUIRED)
find_package(smach_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(std_srvs REQUIRED)

ament_python_install_package(${PROJECT_NAME})

ament_export_dependencies(
  rclpy
  smach
  smach_msgs
  std_msgs
  std_srvs
)

ament_package()

hydra_cpack_ros(
  VERSION ${HYDRA_CPACK_VERSION}
  DEPENDS "ros-humble-smach, ros-humble-smach-msgs"
)
