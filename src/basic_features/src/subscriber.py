#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " | I got the following linear velocity in X: %d", data.linear.x)

def listener():
    rospy.init_node('listener', anonymous=False)
    rospy.Subscriber('cmd_vel', Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.loginfo("Inside main from subscriber.py")
    listener()