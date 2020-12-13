#!/usr/bin/env python
from __future__ import print_function 

import sys
import rospy
from std_srvs.srv import *

def usage():
    return "Please provide one boolean value to set a variable in our service..."

def set_bool_client(value):
    rospy.wait_for_service('/set_bool_service')
    try:
        service = rospy.ServiceProxy('/set_bool_service', SetBool)
        req = SetBoolRequest(value)
        resp = service(req)
        print(resp)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        value = bool(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    
    #Run client
    print("Requesting set bool service")
    print("My value sent is: ", value, " and the response was: ", set_bool_client(value))
