# Copyright 2023 DeepX, Inc. All rights reserved.
cmake_minimum_required(VERSION 3.8)
project(smach_ros)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(ament_cmake_ros REQUIRED)

ament_python_install_package(${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  list(APPEND AMENT_LINT_AUTO_EXCLUDE
    ament_cmake_flake8
    ament_cmake_pep257
  )
  ament_lint_auto_find_test_dependencies()
  find_package(ament_cmake_ros REQUIRED)
  find_package(ament_cmake_pytest REQUIRED)

  ament_add_pytest_test(
    test_concurrence
    test/concurrence.py
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 20
  )

  ament_add_pytest_test(
    test_introspection
    test/introspection.py
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 20
  )

  ament_add_pytest_test(
    test_monitor
    test/monitor.py
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 20
  )

  ament_add_pytest_test(
    test_ref_server
    test/ref_server.py
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 20
  )

  ament_add_pytest_test(
    test_sequence
    test/sequence.py
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 20
  )

  ament_add_pytest_test(
    test_simple_action_timeout
    test/simple_action_timeout.py
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 20
  )

  ament_add_pytest_test(
    test_simple_action
    test/simple_action.py
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 20
  )

  ament_add_pytest_test(
    test_smach_action_server
    test/smach_action_server.py
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 20
  )

  ament_add_pytest_test(
    test_state_machine
    test/state_machine.py
    APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
    TIMEOUT 20
  )

ament_export_dependencies(ament_cmake_pytest)
ament_export_dependencies(ament_cmake_python)
ament_export_dependencies(ament_cmake_ros)

endif()

ament_package()
