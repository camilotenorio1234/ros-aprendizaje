#!/usr/bin/env python3
# SUSCRIPTOR: escucha /chatter y muestra lo que llega.
import rospy
from std_msgs.msg import String

def callback(msg):
    # Se ejecuta cada vez que llega un mensaje
    rospy.loginfo(f'recibi: {msg.data}')

def main():
    rospy.init_node('listener')
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()                                    # mantiene el nodo vivo

if __name__ == '__main__':
    main()
