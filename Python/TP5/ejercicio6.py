# Escribir un programa que cree un diccionario vacío y lo vaya llenando con información sobre una
# persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida a un usuario.
# Cada vez que se añada un nuevo dato debe imprimirse el contenido completo del diccionario.
datos = {}
datos['Nombre'] = input('Ingrese su nombre: ')
print(datos['Nombre'])

datos['Edad'] = input('Ingrese su edad: ')
print(datos['Nombre'] , ' tiene ' , datos['Edad'] , ' años ')
datos['Sexo'] = input('Ingrese su sexo: ')
print(datos['Nombre'] , ' tiene ' , datos['Edad'] , ' años ' , ', su sexo es ' , datos['Sexo'])
datos['Teléfono'] = input('Ingrese su teléfono: ')
print(datos['Nombre'] , ' tiene ' , datos['Edad'] , ' años ' , ', su sexo es ' , datos['Sexo'] , ', su número de telefono es ' , datos['Teléfono'])
datos['Correo'] = input('Ingrese su correo: ')
print(datos['Nombre'] , ' tiene ' , datos['Edad'] , ' años ' , ', su sexo es ' , datos['Sexo'] , ', su número de telefono es ' , datos['Teléfono'] , ' y su correo es ' , datos['Correo'])