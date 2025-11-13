edad = int(input("escriba su edad"))
#nivel = (input("escriba su nivel educativo"))
estutra = int(input("si estudia colocar 1 si trabaja colocar 2 si no trabaja colocar 3"))

if edad > 60 and estutra == 3:
    
    print("adulto mayor jubilado")
    
elif edad > 25 and estutra == 2 :
    
    print("adulto activo")
    
elif 18<= edad <= 25 and estutra == 1:
    
    print("universitario")
    
elif 6 <= edad <= 17 and estutra == 1:
    
    print("estudiante escolar")
    
elif edad < 6 :
    
    print("infante")
    
else: 
    print("no determinado")