# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de
# años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
inversion = float(input('Ingrese la cantidad de dinero a invertir: '))
interes = float(input('Ingrese el interés anual: '))
año = int(input('Ingrese la cantidad de años: '))
for i in range(1 , año + 1):
    capital = (inversion * (interes / 100) + inversion)
    inversion = capital
    print('El capital obtenido en el año ', i , 'fué de: $' , capital)