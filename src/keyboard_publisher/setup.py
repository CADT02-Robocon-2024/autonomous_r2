from setuptools import setup

package_name = 'keyboard_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cadt-02',
    maintainer_email='vandara.gnep@student.cadt.edu.kh',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'keyboard_publisher = keyboard_publisher.keyboard_publisher:main',
            'smart_driver_test = keyboard_publisher.smart_driver_test:main',
            'silo_test = keyboard_publisher.silo_test:main',
        ],
    },
)
