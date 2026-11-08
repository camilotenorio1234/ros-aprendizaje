# ros-aprendizaje

Aprendiendo **ROS 1** y **ROS 2** desde cero con Docker: guías, ejemplos de código y bitácora, con la meta de programar robots humanoides.

![ROS 1: teleop_turtle publica en /turtle1/cmd_vel y turtlesim escucha](docs/img/04-ros1-turtlesim-rqt-graph.png)

*Primer sistema ROS 1 funcionando: tortuga simulada, cuatro terminales y el grafo de nodos (`rqt_graph`).*

## Qué hay aquí

| Carpeta | Contenido |
|---|---|
| [`docker/`](docker/README.md) | Entorno completo en Docker (ROS 1 Noetic + ROS 2 Jazzy) y cómo ejecutarlo |
| [`ros1/`](ros1/GUIA_ROS1.md) | Guía por lecciones de ROS 1 y el workspace `catkin_ws` con paquetes de ejemplo |
| [`ros2/`](ros2/) | Workspace `ros2_ws` para ROS 2 (en preparación) |
| [`docs/`](docs/bitacora.md) | Bitácora de aprendizaje y capturas de pantalla |

## Inicio rápido

Requisitos: Windows con [Docker Desktop](https://www.docker.com/products/docker-desktop/) (backend WSL 2) y unos 10 GB libres.

```powershell
git clone https://github.com/<tu-usuario>/ros-aprendizaje.git
cd ros-aprendizaje\docker
docker compose up -d ros1
```

Abre <http://127.0.0.1:6081> (usuario `ubuntu`, contraseña `ubuntu`) y sigue la [Guía ROS 1](ros1/GUIA_ROS1.md).
Para ROS 2: `docker compose up -d ros2` y <http://127.0.0.1:6080>.

Todos los detalles, capturas y solución de problemas están en [`docker/README.md`](docker/README.md).

## Ruta de aprendizaje

- [x] Entorno Docker con ROS 1 y ROS 2
- [x] ROS 1, Lección 1: nodos, topics y turtlesim
- [ ] ROS 1, Lecciones 2 a 7: workspace, publicador/suscriptor, servicios, launch files
- [ ] ROS 2: nodos, topics, servicios y `colcon`
- [ ] URDF, `tf`, RViz y Gazebo
- [ ] `ros_control` y MoveIt 2
- [ ] Proyecto: robot humanoide

## Versiones

| | Distribución | Ubuntu | Imagen Docker |
|---|---|---|---|
| ROS 1 | Noetic (fin de soporte en 2025; solo para aprender) | 20.04 | `tiryoh/ros-desktop-vnc:noetic` |
| ROS 2 | Jazzy (LTS hasta 2029) | 24.04 | `tiryoh/ros2-desktop-vnc:jazzy` |

Las imágenes son de [Tiryoh](https://github.com/Tiryoh/docker-ros2-desktop-vnc) y dan un escritorio Ubuntu accesible desde el navegador.
