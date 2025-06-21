# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
# rectángulo como el de más abajo, de altura el número introducido.

entero = int(input('Ingrese un número entero: '))
#lista = ['*']
lista = '*'
for i in range(1 , entero + 1):
#    print(f'{" *"*i}')
#    print(lista)
    lista = lista + '*'
    print(lista)
#    lista.append('*')
  
