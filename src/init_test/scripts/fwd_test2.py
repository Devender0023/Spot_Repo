#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


# Creating the node
rospy.init_node('test2')

# Creating the twist messagE object
twist = Twist()

#COnfiguring the params
twist.linear.x=-0.5

rate = rospy.Rate(400)

#Creating the publisher
publisher = rospy.Publisher('/cmd_vel',Twist,queue_size=1)

while not rospy.is_shutdown():
# Publishing the message
    publisher.publish(twist)
    rate.sleep()
