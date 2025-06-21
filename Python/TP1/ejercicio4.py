# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajo = float(input('Ingrese la cantidad de horas trabajadas: '))
coste_horas = float(input('Ingrese la paga por hora: '))
paga = horas_trabajo * coste_horas
print('El pago correspondiente es de $' , paga)