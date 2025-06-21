# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al
# usuario por la contraseña hasta que introduzca la contraseña correcta.
contra = 'contraseña'
contraseña = str(input('Ingrese la contraseña: '))
while contra != contraseña:
    confirmacion = str(input('Contraseña incorrecta, intente de nuevo: '))
    contraseña = confirmacion
print('Bienvenido')