@echo off
cd /d "%~dp0"
echo Iniciando ROS 1 Noetic ... (la primera vez descarga varios GB, puede tardar)
docker compose up -d ros1 > "%~dp0log-ros1.txt" 2>&1
type "%~dp0log-ros1.txt"
echo.
if errorlevel 1 (
  echo ERROR: revisa que Docker Desktop este abierto. Detalle en log-ros1.txt
) else (
  echo ROS 1 Noetic listo: http://127.0.0.1:6081  usuario ubuntu / clave ubuntu
  start http://127.0.0.1:6081
)
pause
