#!/usr/bin/env python3
# SERVICIO: recibe dos numeros (a, b) y responde con la suma.
import rospy
from rospy_tutorials.srv import AddTwoInts, AddTwoIntsResponse

def manejar(req):
    rospy.loginfo(f'sumando {req.a} + {req.b}')
    return AddTwoIntsResponse(req.a + req.b)

def main():
    rospy.init_node('servidor_suma')
    rospy.Service('sumar', AddTwoInts, manejar)
    rospy.loginfo('Servicio /sumar listo')
    rospy.spin()

if __name__ == '__main__':
    main()
