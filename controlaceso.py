usuario = input("escriba su numero de usuario")
code_num = int(input("escriba su codigo"))
result = code_num % 2 
lista = ["james","jose","juan"]


if usuario in lista:
    print("estas en la lista restringida")
elif result == 0 or str(code_num)[-1] == '7':
    print("tienes acceso")
else:
    print("no tiene acceso por que no es multiplo de 2 o el ultimo numero es 7")