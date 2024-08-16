from setuptools import setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, 'script_cam'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vandara',
    maintainer_email='116241847+aradnav@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = script_cam.my_node:main',
            'live_detection_node = script_cam.live_detection_node:main',
            'main = script_cam.main:main',
            'reinforcement_r2 = script_cam.reinforcement_r2:main',
            'get_dist = script_cam.get_dist:main',
            'camera = camera.silo_mover:main',
        ],
    },
)
