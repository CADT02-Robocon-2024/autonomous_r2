from setuptools import setup

package_name = 'odometry_cont'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, 'script_odom'],
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
            'odometry_cont = script_odom.odometry:main'
        ],
    },
)
