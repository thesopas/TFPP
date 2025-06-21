# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta
# atrás desde ese número hasta cero separados por comas.

entero = int(input('Ingrese un numero entero positivo: '))
lista = [entero]
while entero > 0:
    entero = entero - 1
    lista.append(entero)
print(lista)