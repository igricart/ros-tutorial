#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def talker():
    vel = Twist()
    vel.linear.x = 5
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('my_vel_publisher', anonymous=False)
    rate = rospy.Rate(10) #Hz
    while not rospy.is_shutdown():
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    print("Inside main from publisher.py")
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
