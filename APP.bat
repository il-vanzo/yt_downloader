@echo off
SETLOCAL

REM -- Define el directorio base donde se encuentran los scripts Python
set BASE_DIR=%~dp0

REM -- Establecer la ruta al entorno virtual y al script de Python
set VENV_PATH=%BASE_DIR%venv\Scripts\python

REM -- Comprobar si el entorno virtual existe
if not exist "%VENV_PATH%" (
    echo Virtual environment not found. Installing...
    python %BASE_DIR%installer.py
) else (
    REM -- Comprobar si PyTube está instalado en el entorno virtual
    %VENV_PATH% -c "import pytube" 2>NUL
    if errorlevel 1 (
        echo PyTube is not installed in the virtual environment. Reinstalling...
        python %BASE_DIR%installer.py
    ) else (
        echo Virtual environment and PyTube found. Running the downloader...
        call %VENV_PATH% %BASE_DIR%run.py
    )
)

pause
ENDLOCAL
