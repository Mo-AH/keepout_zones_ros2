# Ros2 - Nav2 : Keepout zones in a simulated environment

## Introduction
Navigation in ROS2 with [Nav2](https://navigation.ros.org/) introduced a lot of new features and possibilities. The goal of this ros2 package is to test the feature of navigating in a known environment where the robot cannot pass by some dangerous areas (keepout zones).

## Installation
This package requires a distribution of Ros2 installed, together with the Navigation2 stack and the Webots simulator.

Install the Nav2 stack:
```bashscript
sudo apt install ros-<ros2-distro>-navigation2
```
Install Webots:
```bashscript
sudo snap install webots

sudo apt update

sudo apt install ros-<ros2-distro>-webots-ros2
```

In order to get and build the package, the following commands can be used:
```bashscript
mkdir -p ~/keepout_ws/src

cd ~/keepout_ws/src

git clone https://github.com/Mo-AH/keepout_zones

cd ~/keepout_ws

colcon build --symlink-install 
```

Source the workspace by adding the following line to the .bashrc script.
```bashscript
source ~/keepout_ws/install/local_setup.bash
```


## Run
Once the package has been built and sourced, the simulation can be runned with the following command, that runs the main launch:

```bashscript
ros2 launch keepout_zones robot_launch.py
```

This will start the simulation with a default mask for the keepout zones. The package provides three additional masks in the `maps` folder, that can be tested with a line like this:

```bashscript
ros2 launch keepout_zones robot_launch.py mask:=src/keepout_zones/maps/mask1.yaml
```

The robot initial pose is already set by a script (`inital_pose.py`) launched by `robot_launch.py` and to test the robot navigation with the keepout zones, a goal can be set in Rviz with the `Nav2 Goal` button.

