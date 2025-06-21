#Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable, pregunte
# al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el 
# usuario coincide por la guardada en la variable sin tener en cuenta mayúsculas y 
# minúsculas.
contraseña_1 = str(input('Ingrese una contraseña: '))
contraseña_2 = str(input('Ingrese de nuevo la contraseña: '))
while contraseña_1 != contraseña_2:
    print('Las contraseñas no coinciden, intente de nuevo: ')
    contraseña_2 = str(input())
print('Contraseña actualizada')