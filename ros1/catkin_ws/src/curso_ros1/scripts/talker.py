#!/usr/bin/env python3
# PUBLICADOR: envia un texto al topic /chatter una vez por segundo.
import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('talker')                       # 1. nombre del nodo
    pub = rospy.Publisher('chatter', String, queue_size=10)  # 2. topic y tipo
    rate = rospy.Rate(1)                            # 3. 1 Hz
    n = 0
    while not rospy.is_shutdown():
        msg = f'hola ROS, mensaje {n}'
        rospy.loginfo(msg)
        pub.publish(msg)
        n += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
