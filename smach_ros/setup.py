#!/usr/bin/env python3
import os
from glob import glob
from setuptools import setup

package_name = 'smach_ros'

setup(
    name=package_name,
    version='2.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Isaac I. Y. Saito',
    maintainer_email='gm130s@gmail.com',
    description='SMACH is a task-level architecture for rapidly creating complex robot behavior.',
    license='BSD',
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
)
