# tb3_with_om_moveit_examples
Example code for TurtleBot3 with Open Manipulator using MoveIt

It is assumed that all packages have been installed and setup correclty as per the TurtleBot3 eManual.

Example run command:
rosrun tb3_with_om_moveit_examples control_gripper.py

It has been designed to run on Gazebo and not tested on real hardware.
# Code to launch
roslaunch turtlebot3_manipulation_gazebo turtlebot3_manipulation.launch
roslaunch turtlebot3_manipulation_moveit_config move_group.launch
(Press play in Gazebo window)
roslaunch turtlebot3_manipulation_moveit_config moveit_rviz.launch (optional)
rosrun tb3_with_om_moveit_examples planning_joint_space_goal.py
