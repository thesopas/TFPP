# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de 
# de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario
# la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, 
# si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.

edad = int(input('Ingrese su edad: '))
if edad < 4:
    print('Pasa gratis')
elif edad >= 4 and edad <= 18:
    print('Debe pagar $500')
else:
    print('Debe pagar $1000')
