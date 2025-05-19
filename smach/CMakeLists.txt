cmake_minimum_required(VERSION 3.5)

if(DEFINED HYDRA_CPACK_VERSION)
  set(PROJECT_VERSION ${HYDRA_CPACK_VERSION})
else()
  set(PROJECT_VERSION "0.0.0")
endif()

set(${PROJECT_NAME}_VERSION ${PROJECT_VERSION})
project(${PROJECT_NAME}
  VERSION ${PROJECT_VERSION}
  DESCRIPTION "SMACH is a task-level architecture for rapidly creating complex robot behavior."
)

set(CPACK_PACKAGE_VERSION ${PROJECT_VERSION})

find_package(hydra_cpack REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package(${PROJECT_NAME})

ament_package()

hydra_cpack_ros()
