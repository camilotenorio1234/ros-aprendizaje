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
- Lección 2: compilar el workspace `catkin_ws` y el paquete `curso_ros1`. (Hecha, ver abajo)

**Leccion 2** ([ver](../ros1/lecciones/leccion-02-workspace/README.md))
- Compile el workspace `catkin_ws` con `catkin_make` y active el workspace con `source devel/setup.bash`.
- `rospack find curso_ros1` encontro el paquete; cree `mi_paquete` con `catkin_create_pkg`.
- Aprendido: un workspace tiene `src/`, `build/` y `devel/`; `package.xml` declara dependencias y `CMakeLists.txt` lo que se instala.
- Problema: el contenedor viejo apuntaba a la carpeta anterior (`ls: cannot open directory '.'`). Solucion: `docker rm -f ros1-noetic` y recrearlo con `docker compose up -d ros1` desde la carpeta nueva.
- Siguiente: Leccion 3 (publicador y suscriptor en Python).
