entrada_usuario = ""
while not entrada_usuario.strip():
    entrada_usuario = input("Por favor, introduce tu nombre (no puede estar vacío): ")
    if not entrada_usuario.strip():
        print("¡La entrada está vacía o solo contiene espacios! Inténtalo de nuevo.")

print(f"Hola, {entrada_usuario.strip()}! Bienvenido.")