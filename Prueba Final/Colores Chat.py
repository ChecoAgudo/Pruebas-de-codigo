import random
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

def generar_nombre_usuario():
    return f"Usuario_{random.randint(100, 999)}"

def obtener_nombre_usuario():
    print(Fore.BLUE + "Ingresa tu nombre o pulsa ENTER para generar uno automático:")
    nombre = input("> ").strip()
    if not nombre:
        nombre = generar_nombre_usuario()
    
    print(Fore.GREEN + f"\n✅ Bienvenido al chat, {nombre}")
    return nombre

if __name__ == "__main__":
    obtener_nombre_usuario()
