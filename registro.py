data = []
nombre = ""
while nombre != "fin":
    
    nombre = input("ingrese su nombre")
    
    if nombre == "fin":
        duplicados = []
        
        print(data)
        
        continue
        
    data.append(nombre)
    
    print(data)
    
            #if duplicados == len(data) != len(set(data)):
                
            #print("hay duplicados")