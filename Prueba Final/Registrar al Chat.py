import random

def generarNombreUsuario():
    return f"Usuario_{random.randint(100, 999)}"

def obtenerNombreUsuario():
    nombre = input("Ingresa tu nombre o pulsa ENTER para generar uno automático: ").strip()
    if not nombre:
        nombre = generarNombreUsuario()
    print(f"\n{nombre} ingreso al chat")
    return nombre

if __name__ == "__main__":
    obtenerNombreUsuario()