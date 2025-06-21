# Ingrese un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.
numero_1 = float(input('Ingrese un número: '))
numero_2 = float(input('Ingrese otro número: '))
if numero_2 == 0:
    print('Error: la división por cero no está definida')
else:
    division = numero_1 / numero_2
    print(division)