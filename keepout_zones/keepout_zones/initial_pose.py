import os

def main():
    os.system ( "ros2 topic pub -1 /initialpose geometry_msgs/PoseWithCovarianceStamped '{ header: {stamp: {sec: 0, nanosec: 0}, frame_id: 'map'}, pose: { pose: {position: {x: 0.1, y: 0.0, z: 0.0}, orientation: {w: 0.1}}, } }' ")

if __name__ == '__main__':
    main()