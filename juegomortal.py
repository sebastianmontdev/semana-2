input("presione enter para empezar")
opcion_menu = 0
cuentas = {"sebas" : "123"}
sesion_iniciada = "off"
while sesion_iniciada == "off":

    usuario = input("tienes una cuenta? responder si/no")

    if usuario == "no":

        usuario_A =  str(input("ingrese su usuario"))
        if not usuario_A.strip():
            print("entrada vacia ")
            continue
        contraseña = str(input("ingrese su contraseña"))
        if not usuario_A.strip():
            print("entrada vacia ")
            continue
        cuentas[usuario_A] = contraseña

    elif(usuario == "si"):
        print("ingrese usuario y contraseña")

        usuario_A =  str(input("ingrese su usuario"))
        if not usuario_A.strip():
            print("entrada vacia")
            continue
        contraseña = str(input("ingrese su contraseña"))
        if not contraseña.strip():
            print("entrada vacia ")
            continue
        if usuario_A in cuentas:
            if cuentas[usuario_A] == contraseña:
                print("usuario activo")
                sesion_iniciada = "on"
                break
            elif cuentas[usuario_A] != contraseña:
                print("contraseña incorrecta")
        elif usuario_A not in cuentas:
            print("el usuario no exite")
    else:
        print("ingrese si o no")

while sesion_iniciada == "on":
    print("\n--- Menú del Juego ---")
    print("1. Iniciar Juego")
    print("2. Ver Instrucciones")
    print("3. Salir")
    menu_ingreso = int(input("ingrese una opcion"))

    match(menu_ingreso):
        case 1:
            #me tiene que llamar a la creacion del personaje
            print("Escoja un persona")
            personaje = {"Vida": 100, "Ataque": 200 , "Defensa": 10}
            personaje2 = {"Vida": 100, "Ataque": 10 , "Defensa": 100}
            personaje3 = {"Vida": 200, "Ataque": 30 , "Defensa": 10}
            print(f"PERSONAJE 1: {personaje}")
            print(f"PERSONAJE 2: {personaje2}")
            print(f"PERSONAJE 3: {personaje3}")
            escoger_persona = int(input(":  "))
        case 2:
            #mostrar las instrucciones del juego
            print("")
        case 3:
            print("saliste del juego")
            break