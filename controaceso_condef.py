usuario = int(input("escriba su numero de usuario"))
code_num = int(input("escriba su codigo"))

def es_multiplo(code_num ):
    if (code_num % 2) == 0:
        return True
    else:
        return False

if es_multiplo(code_num):
    
    print("el numero es multiplo de 2")
else:
    print("MEwoq")
