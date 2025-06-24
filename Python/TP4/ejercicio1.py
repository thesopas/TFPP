# Escribir un programa que pida al usuario que ingrese su número de teléfono celular en formato
#internacional (ej: +54 9 381 3849277) y mostrarlo por pantalla en formato local (ej: 153849277).

telefono = str(input('Ingrese su número de telefono en formato internacional, por ej: +54 9 381 3849277: '))
print(len(telefono))
while len(telefono) < 13:
    telefono = str(input('El formato es incorrecto, intente de nuevo: '))

print('Su numero de teléfono en formato local es: 15' , telefono[6:])


