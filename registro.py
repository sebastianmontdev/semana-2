#declaramos las variables
data = []
nombre = ""
#iniciamos el while hasta que nombre sea fin
while nombre != "fin":
    #le pedimos al usuario el nombre que se va a guardar
    nombre = input("ingrese su nombre")
    #con esto revisamos si el valor no esta vacio y si lo esta advertimos al usuario
    if not nombre.strip():
            print("¡La entrada está vacía o solo contiene espacios! Inténtalo de nuevo.")
    #si valor es fin entonces termina el programa y muestra los valores 
    #guardados en nombre
    elif nombre == "fin":
        #aqui comparamos si dentro de data hay resultados iguales
        #mostramos el contenido de data y si hay resultados iguales
        if len(data) != len(set(data)):
            print(data)
            print("hay duplicados")
            #si no hay resultados iguales se muestra el contenido de data
        else:
            print(data)
        
        continue
    else:
        #se guardan los nombres en data
        data.append(nombre)