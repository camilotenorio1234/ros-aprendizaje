# Bitácora de aprendizaje

## 2026-11-07

Leccion completa: [Leccion 1](../ros1/lecciones/leccion-01-turtlesim/README.md)

**Hecho**
- Entorno Docker con ROS 2 Jazzy y ROS 1 Noetic, con escritorio en el navegador.
- ROS 1, Lección 1: `roscore`, `turtlesim`, `turtle_teleop_key`, `rostopic`, `rosnode` y `rqt_graph`.
- Publiqué a mano en `/turtle1/cmd_vel` con `rostopic pub`.

**Aprendido**
- Un nodo publica o escucha en un topic; `rqt_graph` muestra quién es quién.
  En `/turtle1/cmd_vel`, `/teleop_turtle` **publica** y `/turtlesim` **escucha**.
- `roscore` debe estar corriendo antes que cualquier otro nodo de ROS 1.
- En cada terminal nueva hay que hacer `source /opt/ros/noetic/setup.bash`.
- `rostopic echo` imprime sin parar: hay que detenerlo con `Ctrl+C` antes de usar ese panel para otra cosa.

**Problemas y soluciones**
- La descarga de la imagen de ROS 1 falló con un error de DNS (`no such host`). Se resolvió reintentando.
- Ejecuté `docker exec` antes de crear el contenedor: primero va `docker compose up -d`.
- Ejecuté `rqt_graph` en el panel donde corría el teclado y el nodo terminó: un panel = un proceso.

**Siguiente**
- Lección 2: compilar el workspace `catkin_ws` y el paquete `curso_ros1`.
