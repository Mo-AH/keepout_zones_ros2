# Ros2 + Nav2: Keepout zones in a simulated environment

## Introduction
Navigation in ROS2 with [Nav2](https://navigation.ros.org/) introduced a lot of new features and possibilities. The goal of this ros2 package is to test the feature of navigating in a known environment where the robot cannot pass by some dangerous areas (keepout zones).
The goal of this assignment is to apply Nav2, in particular to understand how to use the costmap filter to set up keepout zones. 
We implemented a 3D model of the mobile robot TIAGo in order to run in a personalized 3D world, built using Webots simulator. 
Furthemore, a 2D map is passed to Nav2 through the use of the Map Server node. 


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



## Nodes
### 1. Navagation_launch_file_nodes:

- Nav2 Controller
This is a Task Server in Nav2 that implements the nav2_msgs::action::FollowPath action server which is resposible for generating command velocities for the robot and 
given the computed path from the planner module in nav2_planner.
- Nav2_recoveries
Package that implements a module for executing simple controlled robot movements such as rotating on its own axis or moving linearly.
- BT Navigator
This implements the NavigateToPose task interface. 
It is a Behavior Tree-based implementation of navigation that is intended to allow for flexibility in the navigation task and provide a way to easily 
specify complex robot behaviors.
- Nav2 Waypoint Follower
The Nav2 waypoint follower is a waypoint following program used if you need to go to a given location and complete a specific task,
that is to take a given set of waypoints and navigate to a set of positions in the order provided in the action request. 
The last waypoint in the waypoint array is the final position.
- Nav2 Planner
This is a planning module which implements the nav2_behavior_tree::ComputePathToPose interface which is responsible for generating a feasible 
path, given start and end robot poses.

### 2. slam_launch and localization

- Map Server
The Map Server provides maps to the rest of the Nav2 system using both topic and service interfaces.
- nav2_amcl 
Adaptive Monte Carlo Localization (AMCL) is a probabilistic localization module which estimates the position and orientation (i.e. Pose) of a robot in a given known map.

### 3. bringup_lanuch (file used for control the whole navigation and localization codes)

- costmap_filter_info_server
This is used for filter map which is drawn to be kept out when the robot moves ub the map.
- nav2_lifecycle_manager 
This is used to allows the system startup to ensure that all required nodes have been instantiated correctly before they begin their execution. 
Using lifecycle nodes also allows nodes to be restarted or replaced on-line.

### 4. robot_launch_file

- This file is used for launching the Rviz, tiago robot, the map without keepoutzones, webots environment and bringup file which is reposiblle for the navigation and keepout zones 



