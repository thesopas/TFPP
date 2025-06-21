# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo
# o no.
entero = int(input('Ingrese un número entero: '))
divisor = entero
contador = 0
if entero > 1:
    for i in range(1 , entero + 1):
        resto = entero % divisor 
        divisor = divisor - 1
        if resto == 0:
            contador = contador + 1
if contador == 2:
    print('Es un número primo')
else:
    print('No es un número primo')