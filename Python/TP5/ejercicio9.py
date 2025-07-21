# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se
# almacenarán en un diccionario donde la clave de cada registro será el número de factura y el valor el
# monto de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una
# existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su
# monto y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura
# y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la
# cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
pendiente = 0
pagado = 0
accion = ''
facturas = {'3456':1230}

print('Facturas impagas')
print('-----------------')
print(f"{'Número' : <10} {'Monto' : >10}")
for i in facturas:
    print(f"{i : <10} {'$' : >10} {facturas[i] : >10}")
    pendiente = pendiente + facturas[i]
print('-----------------')
print('Faltan cobrar $' , pendiente)
print('Cantidad cobrada $' , pagado)
print('-----------------')
pendiente = 0

while True:

    print('-----------------')
    print('¿Qué desea hacer?:')
    print('1 - Añadir una factura')
    print('2 - Pagar una factura')
    print('3 - Terminar')
    accion = int(input('seleccione una opción: '))
    print('-----------------')

    if accion == 3:
        break
    elif accion == 1:
        print('-----------------')
        nombre = input('Ingrese el número de la facutura: ')
        facturas[nombre] = float(input('Ingrese el monto de la facutura: '))
        print('-----------------')
    elif accion == 2:
        print('-----------------')
        numero_factura = input('¿Ingrese el número de la factura que desea pagar?: ')
        pagado = pagado + facturas[numero_factura]
        del facturas[numero_factura]
        print('-----------------')
    
    print('Facturas impagas')
    print('-----------------')
    print(f"{'Número' : <10} {'Monto' : >10}")
    for i in facturas:
        print(f"{i : <10} {'$' : >10} {facturas[i] : >10}")
        pendiente = pendiente + facturas[i]
    print('-----------------')
    print('Faltan cobrar $' , pendiente)
    print('Cantidad cobrada $' , pagado)
    print('-----------------')
    print('-----------------')
    pendiente = 0


print('Facturas impagas')
print('-----------------')
print(f"{'Número' : <10} {'Monto' : >10}")
for i in facturas:
    print(f"{i : <10} {'$' : >10} {facturas[i] : >10}")
    pendiente = pendiente + facturas[i]
print('-----------------')
print('Faltan cobrar $' , pendiente)
print('Cantidad cobrada $' , pagado)
print('-----------------')
print('-----------------')
pendiente = 0
