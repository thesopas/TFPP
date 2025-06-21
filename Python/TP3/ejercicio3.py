# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los
# números impares desde 1 hasta ese número separados por comas.

entero = int(input('Ingrese un número entero positivo: '))
for i in range(1 , entero + 1):
    if i % 2 != 0:
        print(i)