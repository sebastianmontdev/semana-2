edad = int(input("escriba su edad"))
licencia = int(input("si tiene licensia ponga 1 si no ponga 2"))
vehiculo = int(input("si su vehiculo es propio o prestamo autorizado escriba 1 si no 2"))

if edad >= 18 and licencia == 1 and vehiculo == 1:
    
    print("es apto")
    
else:
    
    print("no apto")