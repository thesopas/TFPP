# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la división entera entre <n> y
# <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por
# el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = int(input('Ingrese un número: '))
m = int(input('Ingrese otro número: '))

print('La división entera entre ' , n , 'y ' , m , 'es: ' , n // m , 'y su resto es: ' , n % m) 