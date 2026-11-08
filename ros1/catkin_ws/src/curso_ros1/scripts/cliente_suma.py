#!/usr/bin/env python3
# CLIENTE: llama al servicio /sumar.   Uso: rosrun curso_ros1 cliente_suma.py 3 4
import sys
import rospy
from rospy_tutorials.srv import AddTwoInts

def main():
    a = int(sys.argv[1]) if len(sys.argv) > 2 else 2
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    rospy.wait_for_service('sumar')
    sumar = rospy.ServiceProxy('sumar', AddTwoInts)
    resp = sumar(a, b)
    print(f'{a} + {b} = {resp.sum}')

if __name__ == '__main__':
    main()
