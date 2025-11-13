data = []
nombre = ""
while nombre != "fin":
    
    nombre = input("ingrese su nombre")
    if not nombre.strip():
            print("¡La entrada está vacía o solo contiene espacios! Inténtalo de nuevo.")
    elif nombre == "fin":
        if len(data) != len(set(data)):
            print(data)
            print("hay duplicados")
        else:
            print(data)
        
        continue
    else:
        data.append(nombre)
        
    
    
    print(data)