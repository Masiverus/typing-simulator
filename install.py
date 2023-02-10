import sys
import subprocess
import time

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Lista de paquetes necesarios
required_packages = [
    "random",
    "termcolor",
    "pyfiglet",
    "pynput" ,
    "keyboard"
]

# Instalar cada paquete necesario
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)

# Ejecutar el programa
print("Todos los paquetes necesarios han sido instalados correctamente.")
