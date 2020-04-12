#! /usr/bin/env python

#Code taken from Robot Ignite Academy, and also found in multiple locations online.
#Code will make arm move from intial pos, to a different pos, the straight back
#to the initial position

#This code seems to have some bugs. Reports some "INFO" errors during operation. I am
#unable to solve these issues.

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_execute_trajectory', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
arm_group = moveit_commander.MoveGroupCommander("arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

arm_group.clear_pose_targets()
arm_group_variable_values = arm_group.get_current_joint_values()
print "Current Joint Values: %s" %arm_group_variable_values

#Move 1
arm_group_variable_values[0] = 00.00
arm_group_variable_values[1] = 00.00
arm_group_variable_values[2] = 00.00
arm_group_variable_values[3] = 00.00
arm_group.set_joint_value_target(arm_group_variable_values)

plan2 = arm_group.plan()
arm_group.go(wait=True)

#Move 2
arm_group_variable_values[0] = 00.50
arm_group_variable_values[1] = -00.50
arm_group_variable_values[2] = 00.50
arm_group_variable_values[3] = -00.50
arm_group.set_joint_value_target(arm_group_variable_values)

plan2 = arm_group.plan()
arm_group.go(wait=True)

#Move 3
arm_group_variable_values[0] = 00.00
arm_group_variable_values[1] = 00.00
arm_group_variable_values[2] = 00.00
arm_group_variable_values[3] = 00.00
arm_group.set_joint_value_target(arm_group_variable_values)

plan2 = arm_group.plan()
arm_group.go(wait=True)

moveit_commander.roscpp_shutdown()
