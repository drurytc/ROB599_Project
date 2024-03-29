from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'rob599_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name,'resource'), glob(os.path.join('resource', '*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='drurytc',
    maintainer_email='timdrury2020@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'sensor_data = rob599_project.sensor_data:main',
        'servo_control = rob599_project.servo_control:main',
        'classify = rob599_project.classify:main',
        ],
    },
)
