# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un 
# nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al 
# usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = str(input('Ingrese su nombre: '))
sexo = str(input('Ingrese su sexo: '))
if sexo[0].upper() == 'F' and nombre[0].upper() < 'M' or sexo[0].upper() == 'M' and nombre[0].upper() > 'N':
    print('Pertenece al grupo A')
else:
    print('Pertenece al grupo B')


