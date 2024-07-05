from setuptools import setup

package_name = 'movement'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, 'scripts'],
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
            'movement = scripts.movement:main',
            'smart_driver_send = scripts.smart_driver:main'
        ],
    },
)
