@echo off
SETLOCAL

REM -- Define el directorio base donde se encuentran los scripts Python
set BASE_DIR=%~dp0

REM -- Establecer la ruta al directorio del entorno virtual
set VENV_DIR=%BASE_DIR%venv

REM -- Comprobar si el directorio del entorno virtual existe
if not exist "%VENV_DIR%" (
    echo Virtual environment not found. Installing...
    python %BASE_DIR%installer.py
)

REM -- Ejecutar run.py usando el entorno virtual activado
echo Running the downloader...
call %BASE_DIR%venv\Scripts\activate
call %VENV_DIR%\Scripts\python %BASE_DIR%run.py

pause
ENDLOCAL
