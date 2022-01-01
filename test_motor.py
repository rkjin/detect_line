#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist



def fun_callback(msg): 
    pass 

if __name__ == '__main__':
    rospy.init_node('test_motor_node')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)   # topic이름 (sub = pub 이름 동일)


    twist = Twist()

    twist.linear.y = twist.linear.z = 0.0
    twist.angular.x = twist.angular.y = twist.angular.z = 0
    
    while True:
        key = input('Enter key: ')
        if key == '1': 
            twist.linear.x = 1.0
            twist.angular.z = 1.0
            pub.publish(twist)

        elif key == '2':
            twist.linear.x = 1.0
            twist.angular.z = 0.5
            pub.publish(twist)

        elif key == '3':
            twist.linear.x = 1.0
            twist.angular.z = 0.0
            pub.publish(twist)

        elif key == '4':
            twist.linear.x = 1.0
            twist.angular.z = -0.5
            pub.publish(twist)

        elif key == '5':
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)

        elif key == 'q':
            break

    pass