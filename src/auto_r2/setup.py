from setuptools import setup

package_name = 'auto_r2'

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
            'auto_r2 = auto_r2.movement_control:main',
            'rail_control = auto_r2.rail_control:main',
        ],
    },
)
