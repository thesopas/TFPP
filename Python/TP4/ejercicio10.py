# Escriba un programa que permita crea una tupla con los meses del año, pida un número entre 1 y 12 al
# usuario, muestre por pantalla el mes al que se corresponde, y si el número está fuera de rango, se lo
# comunique al usuario
meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Nobiembre', 'Diciembre')
mes = int(input('Ingrese un número entre el 1 y el 12: '))
while mes < 1 or mes > 12:
    mes = int(input('Valor fuera de rango intente de nuevo: '))
mes = mes - 1
for i in range(len(meses)):
    if i == mes:
        print('El mes correspondiente al valor ingresado es: ' , meses[mes])