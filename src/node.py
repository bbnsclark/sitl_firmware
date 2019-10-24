#!/usr/bin/python

import numpy as np
import time

import tf
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Twist

class Node:

    def __init__(self):

        rospy.init_node("FIRMWARE")

        rospy.on_shutdown(self.shutdown)

        rospy.loginfo("Starting node...")

        self.rate = 1.0

        self.pub_tf = tf.TransformBroadcaster()
        
        self.sub_odom = rospy.Subscriber('odom_wheel', Odometry, self.odom_callback)


    def run(self):

        rospy.loginfo("Starting TF broadcast")

        rospy.spin()

    def odom_callback(self, msg):
        

        current_time = rospy.Time.now()
        
        self.pub_tf.sendTransform((msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z), 
        ([msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w]), 
        current_time, "base_link", "odom")
        

    def shutdown(self):

        pass
    
        
if __name__ == "__main__":

    try:

        node = Node()

        node.run()

    except rospy.ROSInterruptException:

        pass

    rospy.loginfo("Exiting")
