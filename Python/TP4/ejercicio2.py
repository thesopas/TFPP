# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y
# muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione
# cuando el día o el mes se introduzcan con un solo carácter.

fecha = str(input('Ingrese su fecha de nacimiento en el orden --> Día, mes, año: '))
print(len(fecha))
comparador = ''
while len(fecha) < 6:
    fecha = str(input('Formato incorrecto, intente de nuevo: '))
while len(fecha) >8:
    fecha = str(input('Formato incorrecto, intente de nuevo: '))
if len(fecha) == 8:
    print('Su fecha de nacimiento es:')
    print(fecha[0:2] , '/' , fecha[2:4] , '/' , fecha[4:])
elif len(fecha) == 7:
    comparador = fecha[0]
    while comparador == '0':
        fecha = str(input('Formato incorrecto, intente de nuevo: '))
        comparador = fecha[0]
    print('Su fecha de nacimiento es:')
    print(fecha[0] , '/' , fecha[1:3] , '/' , fecha[3:])
elif len(fecha) == 6:
    print('Su fecha de nacimiento es:')
    print(fecha[0] , '/' , fecha[1] , '/' , fecha[2:])

# lista = fecha.split('/')


