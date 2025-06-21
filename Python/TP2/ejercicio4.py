#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
entero = int(input('Ingrese un número entero: '))
resto = entero % 2
if resto == 0:
    print('El número es par')
else:
    print('El número es impar')
    