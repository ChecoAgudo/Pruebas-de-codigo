import random
from datetime import datetime

def generarNombreUsuario():
    return f"Usuario_{random.randint(100, 999)}"

def obtenerNombreUsuario():
    nombre = input("Ingresa tu nombre o pulsa ENTER para generar uno automático: ").strip()
    if not nombre:
        nombre = generarNombreUsuario()
    horaActual = datetime.now().strftime("%H:%M:%S")
    print(f"\n✅ Bienvenido al chat, {nombre} (conectado a las {horaActual})")
    return nombre

if __name__ == "__main__":
    obtenerNombreUsuario()