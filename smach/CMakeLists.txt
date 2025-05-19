cmake_minimum_required(VERSION 3.5)
project(deepx_smach
  DESCRIPTION "SMACH is a task-level architecture for rapidly creating complex robot behavior."
)

find_package(hydra_cpack REQUIRED)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package(
  smach
)

ament_package()

hydra_cpack_ros(
    VERSION ${HYDRA_CPACK_VERSION}
)
