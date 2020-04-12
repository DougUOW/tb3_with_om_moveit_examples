#! /usr/bin/env python

#Code taken from Robot Ignite Academy. It perfroms a simple movement in the cartesian plane using moveit.
#Very buggy code at the moment - planner appears to fail periodically. Have also added, in Move3, the ability
#to move the arm to a preset position.

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
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

#Had probelms with planner failing, Using this planner now. I believe default is OMPL
arm_group.set_planner_id("RRTConnectkConfigDefault")
#Increased available planning time from 5 to 10 seconds
arm_group.set_planning_time(10);

#Move 1
pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 1.0
pose_target.position.x = 0.15
pose_target.position.y = 0.0
pose_target.position.z = 0.35
arm_group.set_pose_target(pose_target)

print "Planning path 1"
plan1 = arm_group.plan()
print "Path 1 has been planned"
print "Starting Execution of movement"
arm_group.execute(plan1, wait=True)
print "Movement Finished"
arm_group.stop()
arm_group.clear_pose_targets()

#Move 2
pose_target.orientation.w = 1.0
pose_target.position.x = 0.00
pose_target.position.y = 0.00
pose_target.position.z = 0.35
arm_group.set_pose_target(pose_target)

print "Planning path 2"
plan1 = arm_group.plan()
print "Path 2 has been planned"
print "Starting Execution of movement"
arm_group.execute(plan1, wait=True)
print "Movement Finished"
arm_group.stop()
arm_group.clear_pose_targets()

#Move 3
arm_group.set_named_target("home")
print "Planning path 3"
plan1 = arm_group.plan()
print "Path 3 has been planned"
print "Starting Execution of movement"
arm_group.execute(plan1, wait=True)
print "Movement Finished"
arm_group.stop()
arm_group.clear_pose_targets()
moveit_commander.roscpp_shutdown()
