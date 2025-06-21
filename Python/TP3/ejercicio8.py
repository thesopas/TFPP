# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
# rectángulo como el de más abajo.

entero = int(input('Ingrese un número entero: '))
lista = ''
for i in range(1 , entero):
    if i % 2 == 1:
        lista = lista + ' ' + str(i)
        print(lista[::-1])
