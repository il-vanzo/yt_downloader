import subprocess
import sys
import os

def create_and_activate_venv():
    # Crear un entorno virtual en la carpeta 'venv'
    subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])
    
    # Instalar PyTube en el entorno virtual
    subprocess.check_call(['venv/Scripts/pip', 'install', 'pytube'])

    # Crear carpeta para descargas si no existe
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

if __name__ == "__main__":
    create_and_activate_venv()
    print("PyTube has been installed in the virtual environment and download folder created.")

