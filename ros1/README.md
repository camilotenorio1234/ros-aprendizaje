# ROS 1 (Noetic): curso paso a paso

Cada leccion tiene su carpeta con un README explicado paso a paso, con salidas esperadas y capturas reales.

## Lecciones

| # | Leccion | Estado |
|---|---|---|
| 1 | [Tu primer sistema ROS: nodos, topics y turtlesim](lecciones/leccion-01-turtlesim/README.md) | Hecha |
| 2 | [Workspace catkin y compilar paquetes](lecciones/leccion-02-workspace/README.md) | Hecha |
| 3 | Publicador y suscriptor en Python | Pendiente |
| 4 | Controlar la tortuga con codigo | Pendiente |
| 5 | Servicios | Pendiente |
| 6 | Launch files y parametros | Pendiente |
| 7 | Herramientas utiles (`rqt`, `rosbag`...) | Pendiente |

Los apuntes de las lecciones pendientes estan en [`borrador-lecciones-3-a-7.md`](borrador-lecciones-3-a-7.md).
El codigo de ejemplo esta en [`catkin_ws/src/curso_ros1`](catkin_ws/src/curso_ros1).

## Como trabajar

1. Levanta el entorno (ver [`docker/README.md`](../docker/README.md)):
   ```powershell
   cd docker
   docker compose up -d ros1
   ```
2. Abre <http://127.0.0.1:6081> (usuario `ubuntu`, contrasena `ubuntu`).
3. Dentro del escritorio, abre **Terminator** y trabaja en sus paneles.
4. En **cada** terminal nueva:
   ```bash
   source /opt/ros/noetic/setup.bash
   ```

## Conceptos clave

| Concepto | Que es | Analogia |
|---|---|---|
| Nodo | Programa pequeno que hace una sola tarea | Un empleado especializado |
| Master | `roscore`: directorio donde los nodos se encuentran | La recepcion |
| Topic | Canal con nombre: unos publican, otros escuchan | Una radio con emisor y oyentes |
| Mensaje | El tipo de dato que viaja por un topic | El formato del mensaje |
| Servicio | Pregunta puntual con respuesta | Una llamada telefonica |

Un robot es muchos nodos conversando: camara, motores, planificador...

## Errores comunes

| Mensaje o sintoma | Causa y solucion |
|---|---|
| `command not found: rosrun` | Falta `source /opt/ros/noetic/setup.bash` en esa terminal |
| `Package 'curso_ros1' not found` | Falta `source ~/catkin_ws/devel/setup.bash` (Leccion 2) |
| `Unable to contact my own server` | `roscore` no esta corriendo |
| `Permission denied` al ejecutar un `.py` | Hacer `chmod +x` al script |
| `catkin_make` falla por un enlace simbolico | Ver la [Leccion 2](lecciones/leccion-02-workspace/README.md) (se crea el archivo a mano) |
| El nodo corre pero no recibe nada | El topic tiene otro nombre: revisa `rostopic list` |

## Hacia los humanoides

1. Escribir los mismos nodos en C++ (`rospy` a `roscpp`).
2. `tf`: sistemas de coordenadas y como se relacionan las partes del robot.
3. URDF: describir articulaciones y eslabones.
4. RViz y Gazebo: visualizar y simular un robot.
5. `ros_control`. Despues, pasar a ROS 2: nodos, topics y servicios se mantienen; cambian `colcon`, el lanzamiento y la API.

Referencia oficial: tutoriales en wiki.ros.org (seccion ROS/Tutorials).
