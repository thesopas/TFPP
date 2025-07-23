clientes = {
    12345678 : {
        'Nombre' : 'Juan Pérez',
        'Dirección' : 'Av. Siempre Viva 742',
        'Télefono' : '1112345678',
        'Correo' : 'juan.perez@email.com',
        'Preferente' : True
    },
    23456789: {
        'Nombre' : 'María Gómez',
        'Dirección' : 'Calle Falsa 123',
        'Télefono' : '1123456789',
        'Correo' : 'maria.gomez@email.com',
        'Preferente' : False
    },
    34567890: {
        'Nombre' : 'Carlos López',
        'Dirección' : 'Ruta 9 Km 42',
        'Télefono' : '1134567890',
        'Correo' : 'carlos.lopez@email.com',
        'Preferente' : False
    }
}
print('---------------')
print('1. Añadir cliente')
print('2. Eliminar cliente')
print('3. Mostrar cliente')
print('4. Listar todos los clientes')
print('5. Listar clientes preferentes')
print('6. Terminar')
condicion = int(input('Elija una opción: '))

while True:

    #Terminar
    if condicion == 6:
        print('Saliendo...')
        break
    #Añadir cliente
    elif condicion == 1:
        diccionario_temporal = {}
        diccionario_temporal.clear()
        dni = int(input('Ingrese el DNI del cliente: '))
        diccionario_temporal['Nombre'] = input('Ingrese el nombre completo del cliente: ')
        diccionario_temporal['Direccion'] = input('Ingrese la direccón del cliente: ')
        diccionario_temporal['Telefono'] = input('Ingrese el número de télefono del cliente: ')
        diccionario_temporal['Mail'] = input('Ingrese el mail del cliente: ')
        preferencia = input('¿El cliente es preferente?: ')
        preferencia = preferencia.upper()
        if preferencia == 'SI':
            diccionario_temporal['Preferente'] = True
        elif preferencia == 'NO':
            diccionario_temporal['Preferente'] = False
        clientes[dni] = diccionario_temporal
    #Eliminar cliente
    elif condicion == 2:
        del clientes[int(input('Ingrese el DNI del cliente que desea eliminar: '))]
    #Mostrar cliente
    elif condicion == 3:
        entrada = int(input('Ingrese el DNI del cliente que desea mostrar: '))
        print('---------------')
        for dni, datos in clientes.items():
            if dni == entrada:
                print('DNI: ' , entrada)
                for dato, valor in datos.items():
                    print(f"{dato} {': '} {valor}")
    #Listar clientes
    elif condicion == 4:
        for dni, datos in clientes.items():
            print('---------------')
            print('DNI: ' , dni)
            for dato, valor in datos.items():
                print(f"{dato} {': '} {valor}")
    #Listar clientes preferentes
    elif condicion == 5:
        for dni, datos in clientes.items():
            for dato, valor in datos.items():
                if valor == True:
                  print('---------------')
                  print('DNI:' , dni)
                  for dato2, valor2 in datos.items():
                        print(f"{dato2} {': '} {valor2}")
    else:
        condicion = int(input('Opción incorrecta, intente de nuevo: '))

    print('---------------')
    print('1. Añadir cliente')
    print('2. Eliminar cliente')
    print('3. Mostrar cliente')
    print('4. Listar todos los clientes')
    print('5. Listar clientes preferentes')
    print('6. Terminar')
    condicion = int(input('Elija una opción: '))
