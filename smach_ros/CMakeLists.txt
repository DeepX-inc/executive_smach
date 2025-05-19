cmake_minimum_required(VERSION 3.5)
project(deepx_smach_ros
  DESCRIPTION "Extensions for the SMACH library to integrate it tightly with ROS."
)

find_package(hydra_cpack REQUIRED)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(deepx_smach REQUIRED)
find_package(deepx_smach_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(std_srvs REQUIRED)

ament_python_install_package(
  smach_ros
)

ament_export_dependencies(
  rclpy
  deepx_smach
  deepx_smach_msgs
  std_msgs
  std_srvs
)

ament_package()

hydra_cpack_ros(
  VERSION ${HYDRA_CPACK_VERSION}
  DEPENDS "ros-humble-deepx-smach, ros-humble-deepx-smach-msgs"
)
