#!/usr/bin/env python3
# Hace que la tortuga de turtlesim dibuje un circulo.
# Publica velocidades (Twist) en /turtle1/cmd_vel.
import rospy
from geometry_msgs.msg import Twist

def main():
    rospy.init_node('mover_tortuga')
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    cmd = Twist()
    cmd.linear.x = 1.5     # avanza (m/s)
    cmd.angular.z = 1.0    # gira (rad/s)
    while not rospy.is_shutdown():
        pub.publish(cmd)
        rate.sleep()

if __name__ == '__main__':
    main()
