#!/usr/bin/env python3

import rospy
import math

# import the plan message
from ur5e_control.msg import Plan
from geometry_msgs.msg import Twist


def setup_point(*points):
	plan_point = Twist()
	plan_point.linear.x, plan_point.linear.y, plan_point.linear.z, plan_point.angular.x, plan_point.angular.y, plan_point.angular.z = points
	return plan_point



if __name__ == '__main__':
	# initialize the node
	rospy.init_node('simple_planner', anonymous = True)
	# add a publisher for sending joint position commands
	plan_pub = rospy.Publisher('/plan', Plan, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)

	# define a plan variable
	plan = Plan()
	# declare first point to move to
	plan.points.append(setup_point(-.5, -.14, .4, 3.14, 0.0, 1.5))
	# drop arm to pick up object
	plan.points.append(setup_point(-.5, -.14, 0, 3.14, 0.0, 1.5))
	# pick arm back up
	plan.points.append(setup_point(-.5, -.14, .5, 3.14, 0.0, 1.5))
	# move to position above target
	plan.points.append(setup_point(-.5, -.6, .5, 3.14, 0.0, 1.5))
	# drop arm with object
	plan.points.append(setup_point(-.5, -.6, 0, 3.14, 0.0, 1.5))
	# pick arm back up
	plan.points.append(setup_point(-.5, -.6, .5, 3.14, 0.0, 1.5))

	
	
	while not rospy.is_shutdown():
		# publish the plan
		plan_pub.publish(plan)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
