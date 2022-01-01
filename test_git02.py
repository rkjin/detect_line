#!/usr/bin/env python3
import cv2
import rospy
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge 
from geometry_msgs.msg import Twist


bridge = CvBridge()

def callback(data):
    frame = bridge.imgmsg_to_cv2(data,'bgr8')
    frameb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    left_img1 = frameb[350:450,170:230]
    left_img2 = frameb[350:450,230:290]
    cent_img = frameb[350:450,290:350]
    right_img1 = frameb[350:450,350:410]
    right_img2 = frameb[350:450,410:470]

    cv2.rectangle(frame,(170,350),(230,450),(0,0,255))
    cv2.rectangle(frame,(230,350),(290,450),(0,0,255))
    cv2.rectangle(frame,(290,350),(350,450),(0,0,255))
    cv2.rectangle(frame,(350,350),(410,450),(0,0,255))
    cv2.rectangle(frame,(410,350),(470,450),(0,0,255))

    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
 
    left1 = left_img1.mean()
    left2 = left_img2.mean()
    cent  = cent_img.mean()
    right1 = right_img1.mean()
    right2 = right_img2.mean()
    min = np.argmin([left1, left2, cent, right1, right2])

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)   # topic이름 (sub = pub 이름 동일)
    twist = Twist()

    twist.linear.y = twist.linear.z = 0.0
    twist.angular.x = twist.angular.y = twist.angular.z = 0
    
    if key == 0: 
        twist.linear.x = 1.0
        twist.angular.z = 1.0
        pub.publish(twist)

    elif key == 1:
        twist.linear.x = 1.0
        twist.angular.z = 0.5
        pub.publish(twist)

    elif key == 2:
        twist.linear.x = 1.0
        twist.angular.z = 0.0
        pub.publish(twist)

    elif key == 3:
        twist.linear.x = 1.0
        twist.angular.z = -0.5

        pub.publish(twist)

    elif key == 4:
        twist.linear.x = 1.0
        twist.angular.z = -1.0
        pub.publish(twist)


    else:
        pass


    # pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    # pub.publish(direction)
    return

def main():
    rospy.init_node('planner_node')
    rospy.Subscriber("/cv_camera/image_raw", Image, callback)
    rospy.spin()


if __name__ == '__main__':
    main()

    pass


cv2.destroyAllWindows()