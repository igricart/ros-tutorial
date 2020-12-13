#!/usr/bin/env python

from __future__ import print_function

from std_srvs.srv import SetBool, SetBoolResponse
import rospy

def handle_service_request(req):
    print("I just recieved the following Trigger request: ", req.data)
    return SetBoolResponse(
        success = True,
        message = "Sent the message successfully"
    )

def set_bool_service():
    rospy.init_node('set_bool_server')
    serv = rospy.Service('set_bool_service', SetBool, handle_service_request)
    print("Ready to set a bool")
    rospy.spin()

if __name__ == "__main__":
    set_bool_service()