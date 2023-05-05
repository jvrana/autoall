#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages


setup(
    name='pyautoall',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pyautoall = pyautoall:main',
        ],
    },
)