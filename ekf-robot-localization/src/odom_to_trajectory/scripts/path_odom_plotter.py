#!/usr/bin/env python
from __future__ import print_function
import rospy
from tf.transformations import quaternion_from_euler
from std_msgs.msg import String
from nav_msgs.msg import Odometry, Path
from geometry_msgs import PoseWithCovarianceStamped, PoseStamped
from sensor_msgs.msg import Joy

import sys
import json
from math import sqrt
from collections import deque

import time

def callback(data):
	global xAnt
	global yAnt
	global cont

	#Is created the pose msg, its necessary do it each time because python manages objects by reference, and does not make deep copies unless explicitly asked to do so.
	pose = PoseStamped()

	#Set a atributes of the msg
	pose.header.frame_id = "odom"
	pose.pose.position.x = float(data.pose.pose.position.x)
	pose.pose.position.y = float(data.pose.pose.position.y)
	pose.pose.orientation.x = float(data.pose.pose.orientation.x)
	pose.pose.orientation.y = float(data.pose.pose.orientation.y)
	pose.pose.orientation.z = float(data.pose.pose.orientation.z)
	poes.pose.orientation.w = float(data.pose.pose.orientation.w)


	#To avoid repeating the values, it is found that the recived values are differents
	if(xAnt != pose.pose.position.x and yAnt !=pose.pose.position.y):
		#Set a attributes of the msg
		pose.header.seq = path.header.seq + 1
		path.header.frame_id = "odom"
		path.header.stamp= rospy.Time.now()
		pose.header.stamp= path.header.stamp
		path.poses.append= (pose)

		#Published the msg

	cont = cont+1
	rospy.loginfo("Value Counted: %i" % cont)
	if cont> max_append:
		path.pose.pop(0)
	pub.publish(path)

	#Save the last position
	xAnt=pose.pose.orientation.x
	yAnt=pose.pose.position.y
	return path


if __name__ == '__main__':
	#Variable initialization
	global xAnt
	global yAnt
	global cont
	xAnt = 0.0
	yAnt = 0.0
	cont=0

	#Node and msg initialization
	rospy.init_node('path_odom_plotter')

	#Rosparams that are set in the launch
	#max size of array pose msg from the path
	if not rospy.has_param("~max_list_append"):
		rospy.logwarn('The parameter max_list_append dont exists')
	max_append = rospy.set_param("~max_list_append", 1000)
	max_append = 1000
	if not (max_append > 0):
		rospy.logwarn('The parameter max_list_append not is correct')
		sys.exit()
	pub = rospy.Publisher('/odompath',Path, queue_size=1)

	path = Path()

	msg = Odometry()

	#Subscription to the topic
	msg = rospy.Subscriber('/odom', Odometry, callback)
	rate = rospy.Rate(30)

try:

	while not rospy.is_shutdown():
		rate.sleep()

	except rospy.ROSInterruptException:
		pass


