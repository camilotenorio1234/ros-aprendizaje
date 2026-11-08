@echo off
cd /d "%~dp0"
echo Iniciando ROS 2 Jazzy ... (la primera vez descarga varios GB, puede tardar)
docker compose up -d ros2 > "%~dp0log-ros2.txt" 2>&1
type "%~dp0log-ros2.txt"
echo.
if errorlevel 1 (
  echo ERROR: revisa que Docker Desktop este abierto. Detalle en log-ros2.txt
) else (
  echo ROS 2 Jazzy listo: http://127.0.0.1:6080  usuario ubuntu / clave ubuntu
  start http://127.0.0.1:6080
)
pause
