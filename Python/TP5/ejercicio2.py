# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un
# diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive
# en <dirección> y su número de teléfono es <teléfono>.
datos = {}
datos['Nombre'] = input('Ingrese su nombre: ')
datos['Edad'] = input('Ingrese su edad: ')
datos['Dirección'] = input('Ingrese su dirección: ')
datos['Teléfono'] = input('Ingrese su teléfono: ')

print(datos['Nombre'] , ' tiene ' , datos['Edad'] , ' años, ' , 'vive en ' , datos['Dirección'] , ' y su teléfono es ' , datos['Teléfono'])
