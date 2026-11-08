# Borrador: lecciones 2 a 7 (aun sin realizar)

Apuntes preparados para las proximas lecciones. Cuando hagamos cada una, se convierte en
su propia carpeta `lecciones/leccion-NN-.../README.md` con capturas y salidas reales,
igual que la [Leccion 1](lecciones/leccion-01-turtlesim/README.md).

---------------------------------------------------------------------------
## Leccion 2 - Workspace y compilar el paquete de ejemplos

Un workspace catkin es la carpeta donde viven y se compilan tus paquetes.
Ya tienes `~/catkin_ws/src/curso_ros1` con ejemplos.

IMPORTANTE (una sola vez): la carpeta esta montada desde Windows y ahi no se
pueden crear enlaces simbolicos, asi que creamos el archivo a mano:

    cp --remove-destination /opt/ros/noetic/share/catkin/cmake/toplevel.cmake ~/catkin_ws/src/CMakeLists.txt

Compilar:

    cd ~/catkin_ws
    catkin_make
    source devel/setup.bash           # hacerlo tras CADA compilacion
    rospack find curso_ros1           # debe mostrar la ruta del paquete

Si ves "Permission denied" al ejecutar un script:
`chmod +x ~/catkin_ws/src/curso_ros1/scripts/*.py`

Estructura de un paquete:

    curso_ros1/
    ├── package.xml        <- nombre, dependencias
    ├── CMakeLists.txt     <- como se compila / instala
    ├── scripts/           <- nodos en Python
    └── launch/            <- arranque de varios nodos

---------------------------------------------------------------------------
## Leccion 3 - Publicador y suscriptor (topics)

Lee `scripts/talker.py` y `scripts/listener.py` (tienen comentarios).
Flujo: `init_node` -> crear Publisher/Subscriber -> bucle o `spin`.

    roscore                                   # Terminal 1
    rosrun curso_ros1 talker.py               # Terminal 2
    rosrun curso_ros1 listener.py             # Terminal 3
    rqt_graph                                 # ver la conexion

Ejercicios:
1. Cambia la frecuencia a 5 Hz y recompila (no hace falta recompilar scripts
   Python ya instalados por catkin_make con enlaces; si no ves el cambio,
   vuelve a hacer `catkin_make`).
2. Cambia el topic a `/saludo` en AMBOS nodos. Si solo cambias uno, no se
   hablan: asi se rompen las conexiones en ROS.
3. Ejecuta dos listeners a la vez y mira que ambos reciben todo.

---------------------------------------------------------------------------
## Leccion 4 - Controlar la tortuga con codigo

    roscore
    rosrun turtlesim turtlesim_node
    rosrun curso_ros1 mover_tortuga.py

Publicas `geometry_msgs/Twist` en `/turtle1/cmd_vel`: `linear.x` avanza,
`angular.z` gira. Ese mismo mensaje mueve robots reales.

Ejercicios:
1. Haz que dibuje un circulo mas grande y otro mas pequeno.
2. Modifica el nodo para que avance 3 segundos y luego se detenga.
3. Suscribete a `/turtle1/pose` y muestra la posicion x, y en pantalla.

---------------------------------------------------------------------------
## Leccion 5 - Servicios

    roscore
    rosrun curso_ros1 servidor_suma.py
    rosrun curso_ros1 cliente_suma.py 3 4         # imprime 3 + 4 = 7

Herramientas:

    rosservice list
    rosservice type /sumar
    rosservice call /sumar "a: 10
    b: 5"

Topic = flujo continuo sin respuesta. Servicio = pregunta y respuesta.

Ejercicio: crea un servicio que reciba un numero y devuelva su doble
(pista: reutiliza `rospy_tutorials/AddTwoInts` poniendo b = a, o crea tu .srv).

---------------------------------------------------------------------------
## Leccion 6 - Launch files y parametros

Un launch arranca varios nodos y `roscore` de una vez:

    roslaunch curso_ros1 pubsub.launch
    roslaunch curso_ros1 tortuga.launch

Parametros (configuracion compartida):

    rosparam list
    rosparam get /turtlesim/background_r
    rosparam set /turtlesim/background_r 255
    rosservice call /clear

Ejercicio: crea tu propio `.launch` que arranque talker, listener y turtlesim.

---------------------------------------------------------------------------
## Leccion 7 - Herramientas utiles

    rqt                      # panel con plugins
    rqt_plot /turtle1/pose/x # graficar un valor
    rosbag record -a         # grabar todos los topics
    rosbag play archivo.bag  # reproducirlos
    rosnode info /nombre     # detalle de un nodo
    roswtf                   # diagnostico del sistema
