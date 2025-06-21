# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(1,11):
    print('Tabla del ' , i)
    for b in range(1 , 11):
        multiplicacion = b * i
        print(multiplicacion)