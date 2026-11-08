cmake_minimum_required(VERSION 3.0.2)
project(curso_ros1)

find_package(catkin REQUIRED COMPONENTS rospy std_msgs geometry_msgs rospy_tutorials)

catkin_package()

catkin_install_python(PROGRAMS
  scripts/talker.py
  scripts/listener.py
  scripts/mover_tortuga.py
  scripts/servidor_suma.py
  scripts/cliente_suma.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
