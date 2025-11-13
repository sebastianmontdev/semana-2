cuentas = {
    "juan": "1234",
    "ana": "abcd",
    "pedro": "qwerty"
}
usuario_A = input("Usuario: ")
clave_A = input("Contraseña: ")

if usuario_A in cuentas:  # Primero verifica si el usuario existe
    if cuentas[usuario_A] == clave_A:  # Luego compara la contraseña
        print("Usuario y contraseña correctos")
        sesion_iniciada = "on"
    else:
        print("Contraseña incorrecta")
else:
    print("El usuario no existe")
