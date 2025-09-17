#!/usr/bin/env python3
"""Setup script for Kova Sensor Utils"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
def read_requirements(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Base requirements
requirements = read_requirements("requirements.txt")

# Optional requirements
extras_require = {
    "gpu": [
        "cupy-cuda11x>=10.0.0",
        "numba>=0.56.0",
    ],
    "dev": [
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
        "pytest-asyncio>=0.21.0",
        "black>=23.0.0",
        "isort>=5.12.0",
        "flake8>=6.0.0",
        "mypy>=1.0.0",
        "pre-commit>=3.0.0",
    ],
    "docs": [
        "sphinx>=5.0.0",
        "sphinx-rtd-theme>=1.2.0",
        "sphinx-autodoc-typehints>=1.19.0",
    ],
    "benchmarks": [
        "pytest-benchmark>=4.0.0",
        "memory-profiler>=0.60.0",
    ],
}

setup(
    name="kova-sensor-utils",
    version="0.1.0",
    author="Kova Systems",
    author_email="dev@kovasystems.com",
    description="Python utilities for sensor data processing in the Kova ecosystem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kovasystems/kova-sensor-utils",
    project_urls={
        "Bug Reports": "https://github.com/kovasystems/kova-sensor-utils/issues",
        "Source": "https://github.com/kovasystems/kova-sensor-utils",
        "Documentation": "https://docs.kova.systems/sensor-utils/",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require=extras_require,
    entry_points={
        "console_scripts": [
            "kova-process-image=kova_sensor_utils.cli.image:main",
            "kova-process-pointcloud=kova_sensor_utils.cli.pointcloud:main",
            "kova-process-imu=kova_sensor_utils.cli.imu:main",
            "kova-process-gps=kova_sensor_utils.cli.gps:main",
            "kova-process-thermal=kova_sensor_utils.cli.thermal:main",
            "kova-batch-process=kova_sensor_utils.cli.batch:main",
        ],
    },
    include_package_data=True,
    package_data={
        "kova_sensor_utils": [
            "data/*.json",
            "data/*.yaml",
            "data/*.yml",
        ],
    },
    zip_safe=False,
    keywords=[
        "robotics",
        "sensors",
        "image-processing",
        "point-cloud",
        "imu",
        "gps",
        "thermal",
        "quality-assessment",
        "data-processing",
    ],
)
