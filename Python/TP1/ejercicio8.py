# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de
# años, y muestre por pantalla el capital obtenido en la inversión.
inversion = float(input('Ingrese la cantidad de dinero a invertir: '))
interes = float(input('Ingrese el interés anual: '))
anios = int(input('Ingrese la cantidad de años: '))
capital = (inversion * (interes/100) * anios) + inversion
print('El capital obtenido es $' , round(capital,2))
