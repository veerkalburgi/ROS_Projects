# Start Simulation 
---
    roslaunch turtlebot_navigation_gazebo main.launch

This command spawns the turtlebot and world in gazebo

    roslaunch turtlebot_navigation_gazebo move_base_demo.launch

The second command launch the amcl algorithm for the turtlebot

    roslaunch turtlebot_rviz_launchers view_navigation.launch

The third one launches the rviz tool for visualization

    rosrun setpoint main.py
    
This script, we set the initial point to x,y,z all equal to zero, This will couse robot move to origin of map.

---
