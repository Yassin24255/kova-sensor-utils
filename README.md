# Kova Sensor Utils

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/kova-sensor-utils.svg)](https://pypi.org/project/kova-sensor-utils/)
[![Build Status](https://github.com/kovasystems/kova-sensor-utils/workflows/CI/badge.svg)](https://github.com/kovasystems/kova-sensor-utils/actions)

**Python utilities for sensor data processing in the Kova ecosystem**

Kova Sensor Utils is a comprehensive Python library designed for processing and analyzing sensor data within the Kova decentralized robotics network. It provides tools for image processing, point cloud analysis, IMU data validation, and quality assessment algorithms.

## Features

- **Image Processing**: Advanced image enhancement, filtering, and analysis
- **Point Cloud Processing**: LiDAR data processing and point cloud analysis
- **IMU Data Processing**: Inertial measurement unit data validation and analysis
- **GPS Data Processing**: GPS coordinate processing and validation
- **Thermal Data Processing**: Thermal imaging data analysis
- **Quality Assessment**: Data quality metrics and validation
- **CLI Tools**: Command-line utilities for batch processing
- **Async Support**: Asynchronous processing for high-throughput applications
- **GPU Acceleration**: CUDA support for computationally intensive operations

## Installation

### From PyPI

```bash
pip install kova-sensor-utils
```

### From Source

```bash
git clone https://github.com/kovasystems/kova-sensor-utils.git
cd kova-sensor-utils
pip install -e .
```

### With GPU Support

```bash
pip install kova-sensor-utils[gpu]
```

## Quick Start

### Basic Usage

```python
from kova_sensor_utils import ImageProcessor, PointCloudProcessor, IMUProcessor
import numpy as np

# Image processing
image_processor = ImageProcessor()
enhanced_image = image_processor.enhance('input.jpg', 
                                       brightness=1.2, 
                                       contrast=1.1, 
                                       sharpness=1.05)

# Point cloud processing
pc_processor = PointCloudProcessor()
point_cloud = pc_processor.load('data.pcd')
filtered_pc = pc_processor.filter_outliers(point_cloud, 
                                         method='statistical', 
                                         std_ratio=2.0)

# IMU data processing
imu_processor = IMUProcessor()
imu_data = imu_processor.load('imu_data.csv')
calibrated_data = imu_processor.calibrate(imu_data)
```

### Quality Assessment

```python
from kova_sensor_utils import QualityAssessor, SensorData

# Create quality assessor
assessor = QualityAssessor()

# Assess image quality
image_quality = assessor.assess_image_quality('image.jpg')
print(f"Image quality score: {image_quality.overall_score:.2f}")

# Assess point cloud quality
pc_quality = assessor.assess_point_cloud_quality('pointcloud.pcd')
print(f"Point cloud quality score: {pc_quality.overall_score:.2f}")

# Assess IMU data quality
imu_quality = assessor.assess_imu_quality('imu_data.csv')
print(f"IMU quality score: {imu_quality.overall_score:.2f}")
```

### Batch Processing

```python
from kova_sensor_utils import BatchProcessor, ProcessingConfig

# Configure batch processing
config = ProcessingConfig(
    input_dir='data/raw',
    output_dir='data/processed',
    enable_parallel=True,
    max_workers=4,
    quality_threshold=0.7
)

# Process all sensor data
processor = BatchProcessor(config)
results = processor.process_all()

print(f"Processed {results.total_files} files")
print(f"Success rate: {results.success_rate:.2%}")
```

## API Reference

### Image Processing

```python
from kova_sensor_utils import ImageProcessor, ImageConfig

# Create image processor with configuration
config = ImageConfig(
    target_resolution=(1920, 1080),
    quality_threshold=0.8,
    enable_gpu=True,
    output_format='JPEG'
)

processor = ImageProcessor(config)

# Basic operations
enhanced = processor.enhance('input.jpg')
resized = processor.resize('input.jpg', (640, 480))
rotated = processor.rotate('input.jpg', angle=90)

# Advanced operations
denoised = processor.denoise('noisy_image.jpg', method='bilateral')
sharpened = processor.sharpen('blurry_image.jpg', strength=1.5)
corrected = processor.correct_exposure('dark_image.jpg')

# Batch processing
results = processor.process_batch(['img1.jpg', 'img2.jpg', 'img3.jpg'])
```

### Point Cloud Processing

```python
from kova_sensor_utils import PointCloudProcessor, PointCloudConfig
import numpy as np

# Create point cloud processor
config = PointCloudConfig(
    max_points=1000000,
    min_density=0.1,
    enable_gpu=True
)

processor = PointCloudProcessor(config)

# Load point cloud
pc = processor.load('data.pcd')

# Filtering operations
filtered = processor.filter_outliers(pc, method='statistical')
downsampled = processor.downsample(pc, voxel_size=0.01)
cropped = processor.crop(pc, min_bounds=[0, 0, 0], max_bounds=[10, 10, 5])

# Analysis operations
density = processor.calculate_density(pc)
normals = processor.estimate_normals(pc)
features = processor.extract_features(pc)

# Save processed point cloud
processor.save(filtered, 'filtered.pcd')
```

### IMU Data Processing

```python
from kova_sensor_utils import IMUProcessor, IMUConfig
import pandas as pd

# Create IMU processor
config = IMUConfig(
    sample_rate=100.0,
    enable_calibration=True,
    gravity_threshold=9.8
)

processor = IMUProcessor(config)

# Load IMU data
imu_data = processor.load('imu_data.csv')

# Calibration
calibrated = processor.calibrate(imu_data)
bias_corrected = processor.correct_bias(imu_data)

# Analysis
orientation = processor.calculate_orientation(imu_data)
velocity = processor.integrate_velocity(imu_data)
position = processor.integrate_position(imu_data)

# Quality assessment
quality_metrics = processor.assess_quality(imu_data)
print(f"IMU quality: {quality_metrics.overall_score:.2f}")
```

### GPS Data Processing

```python
from kova_sensor_utils import GPSProcessor, GPSConfig

# Create GPS processor
config = GPSConfig(
    reference_ellipsoid='WGS84',
    enable_dgps=True,
    accuracy_threshold=5.0
)

processor = GPSProcessor(config)

# Load GPS data
gps_data = processor.load('gps_data.csv')

# Coordinate transformations
utm_coords = processor.to_utm(gps_data)
local_coords = processor.to_local(gps_data, reference_point=(0, 0, 0))

# Quality assessment
quality = processor.assess_quality(gps_data)
print(f"GPS accuracy: {quality.accuracy:.2f} meters")
```

### Thermal Data Processing

```python
from kova_sensor_utils import ThermalProcessor, ThermalConfig

# Create thermal processor
config = ThermalConfig(
    temperature_range=(-40, 120),
    emissivity=0.95,
    enable_calibration=True
)

processor = ThermalProcessor(config)

# Load thermal data
thermal_data = processor.load('thermal.raw')

# Temperature analysis
temperature_map = processor.extract_temperature(thermal_data)
hot_spots = processor.detect_hot_spots(thermal_data, threshold=50.0)
temperature_profile = processor.get_temperature_profile(thermal_data)

# Visualization
processor.save_temperature_image(temperature_map, 'temperature.png')
```

## CLI Tools

### Image Processing CLI

```bash
# Enhance image
kova-process-image input.jpg --enhance --brightness 1.2 --contrast 1.1

# Batch process images
kova-process-image data/ --batch --output processed/ --quality-threshold 0.8

# Resize images
kova-process-image input.jpg --resize 640x480 --output resized.jpg

# Denoise image
kova-process-image noisy.jpg --denoise bilateral --output clean.jpg
```

### Point Cloud Processing CLI

```bash
# Filter point cloud
kova-process-pointcloud data.pcd --filter statistical --std-ratio 2.0

# Downsample point cloud
kova-process-pointcloud data.pcd --downsample 0.01 --output downsampled.pcd

# Analyze point cloud
kova-process-pointcloud data.pcd --analyze --density --normals

# Batch process
kova-process-pointcloud data/ --batch --output processed/
```

### IMU Processing CLI

```bash
# Calibrate IMU data
kova-process-imu data.csv --calibrate --output calibrated.csv

# Analyze IMU data
kova-process-imu data.csv --analyze --orientation --velocity

# Quality assessment
kova-process-imu data.csv --quality --threshold 0.8
```

### Batch Processing CLI

```bash
# Process all sensor data
kova-batch-process data/ --output processed/ --parallel --workers 4

# Process specific sensor types
kova-batch-process data/ --sensors camera,lidar --output processed/

# Quality filtering
kova-batch-process data/ --quality-threshold 0.7 --output high-quality/
```

## Configuration

### Image Processing Configuration

```python
from kova_sensor_utils import ImageConfig

config = ImageConfig(
    target_resolution=(1920, 1080),
    quality_threshold=0.8,
    enable_gpu=True,
    output_format='JPEG',
    compression_quality=95,
    enable_metadata=True,
    color_space='sRGB'
)
```

### Point Cloud Configuration

```python
from kova_sensor_utils import PointCloudConfig

config = PointCloudConfig(
    max_points=1000000,
    min_density=0.1,
    enable_gpu=True,
    voxel_size=0.01,
    outlier_std_ratio=2.0,
    normal_estimation_radius=0.05
)
```

### IMU Configuration

```python
from kova_sensor_utils import IMUConfig

config = IMUConfig(
    sample_rate=100.0,
    enable_calibration=True,
    gravity_threshold=9.8,
    bias_correction=True,
    noise_reduction=True,
    integration_method='trapezoidal'
)
```

## Examples

### Complete Sensor Data Pipeline

```python
from kova_sensor_utils import (
    ImageProcessor, PointCloudProcessor, IMUProcessor,
    QualityAssessor, BatchProcessor
)

# Initialize processors
image_processor = ImageProcessor()
pc_processor = PointCloudProcessor()
imu_processor = IMUProcessor()
quality_assessor = QualityAssessor()

# Process image data
image = image_processor.load('camera_data.jpg')
enhanced_image = image_processor.enhance(image)
image_quality = quality_assessor.assess_image_quality(enhanced_image)

if image_quality.overall_score >= 0.8:
    image_processor.save(enhanced_image, 'processed/camera_data.jpg')

# Process point cloud data
pc = pc_processor.load('lidar_data.pcd')
filtered_pc = pc_processor.filter_outliers(pc)
pc_quality = quality_assessor.assess_point_cloud_quality(filtered_pc)

if pc_quality.overall_score >= 0.8:
    pc_processor.save(filtered_pc, 'processed/lidar_data.pcd')

# Process IMU data
imu_data = imu_processor.load('imu_data.csv')
calibrated_imu = imu_processor.calibrate(imu_data)
imu_quality = quality_assessor.assess_imu_quality(calibrated_imu)

if imu_quality.overall_score >= 0.8:
    imu_processor.save(calibrated_imu, 'processed/imu_data.csv')
```

### Real-time Processing

```python
import asyncio
from kova_sensor_utils import AsyncImageProcessor, AsyncPointCloudProcessor

async def process_sensor_data():
    # Initialize async processors
    image_processor = AsyncImageProcessor()
    pc_processor = AsyncPointCloudProcessor()
    
    # Process data concurrently
    tasks = [
        image_processor.process_async('camera_data.jpg'),
        pc_processor.process_async('lidar_data.pcd')
    ]
    
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(f"Processed: {result.filename}, Quality: {result.quality_score:.2f}")

# Run async processing
asyncio.run(process_sensor_data())
```

## Testing

Run all tests:

```bash
pytest
```

Run specific test categories:

```bash
pytest tests/test_image_processing.py
pytest tests/test_point_cloud_processing.py
pytest tests/test_imu_processing.py
pytest tests/test_quality_assessment.py
```

Run with coverage:

```bash
pytest --cov=kova_sensor_utils --cov-report=html
```

## Performance

Kova Sensor Utils is optimized for high-performance sensor data processing:

- **GPU Acceleration**: CUDA support for computationally intensive operations
- **Parallel Processing**: Multi-threaded and async processing capabilities
- **Memory Efficiency**: Streaming processing for large datasets
- **Optimized Algorithms**: Efficient implementations of common sensor processing algorithms

### Benchmarking

```bash
# Run performance benchmarks
python -m kova_sensor_utils.benchmarks

# Benchmark specific operations
python -m kova_sensor_utils.benchmarks image_processing
python -m kova_sensor_utils.benchmarks point_cloud_processing
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Clone your fork
3. Create a virtual environment
4. Install development dependencies
5. Make your changes
6. Add tests
7. Run the test suite
8. Submit a pull request

```bash
git clone https://github.com/your-username/kova-sensor-utils.git
cd kova-sensor-utils
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- [Website](https://www.kova.systems/)
- [Documentation](https://docs.kova.systems/sensor-utils/)
- [Discord](https://discord.gg/kova)
- [Twitter](https://twitter.com/KovaSystems)

## Acknowledgments

- The Python community for excellent scientific computing libraries
- OpenCV team for computer vision capabilities
- PCL team for point cloud processing
- The Kova Systems team for the sensor processing requirements

---

**Made with ❤️ by the Kova Systems team**