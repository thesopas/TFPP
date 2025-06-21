# Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales 
# o superiores a $100.000 mensuales. Escribir un programa que pregunte al usuario su edad y 
# sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
edad = int(input('Ingrese su edad: '))
ingresos = float(input('Ingrese sus ingresos: '))
if edad >= 18 and ingresos >= 100000:
    print('Usted debe tributar')
else:
    print('Usted no debe tributar')