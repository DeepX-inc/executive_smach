cmake_minimum_required(VERSION 3.5)
project(smach
  DESCRIPTION "SMACH is a task-level architecture for rapidly creating complex robot behavior."
)

find_package(hydra_cpack REQUIRED)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package(${PROJECT_NAME})

ament_package()

hydra_cpack_ros()
