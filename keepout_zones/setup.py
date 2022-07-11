from setuptools import setup

package_name = 'keepout_zones'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name, ['package.xml']))

# Launches
data_files.append(('share/' + package_name + '/launch', ['launch/localization_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/navigation_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/slam_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/robot_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/bringup_launch.py']))

# Map and masks 
data_files.append(('share/' + package_name + '/maps', ['maps/map.pgm']))
data_files.append(('share/' + package_name + '/maps', ['maps/map.yaml']))
data_files.append(('share/' + package_name + '/maps', ['maps/default_mask.pgm']))
data_files.append(('share/' + package_name + '/maps', ['maps/default_mask.yaml']))
data_files.append(('share/' + package_name + '/maps', ['maps/mask1.pgm']))
data_files.append(('share/' + package_name + '/maps', ['maps/mask1.yaml']))
data_files.append(('share/' + package_name + '/maps', ['maps/mask2.pgm']))
data_files.append(('share/' + package_name + '/maps', ['maps/mask2.yaml']))
data_files.append(('share/' + package_name + '/maps', ['maps/mask3.pgm']))
data_files.append(('share/' + package_name + '/maps', ['maps/mask3.yaml']))

# Params 
data_files.append(('share/' + package_name + '/params', ['params/nav2_params.yaml']))
data_files.append(('share/' + package_name + '/params', ['params/keepout_params.yaml']))

# Resources
data_files.append(('share/' + package_name + '/resource', ['resource/default.rviz']))
data_files.append(('share/' + package_name + '/resource', ['resource/ros2_control.yml']))
data_files.append(('share/' + package_name + '/resource', ['resource/tiago_webots.urdf']))

# Worlds
data_files.append(('share/' + package_name + '/worlds', ['worlds/default.wbt']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files= data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='momo',
    maintainer_email='momo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'initial_pose = keepout_zones.initial_pose:main'
        ],
    },
)
