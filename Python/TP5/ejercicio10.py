diccionario_temporal = {}
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
        break
    #Añadir cliente
    elif condicion == 1:
        DNI = int('Ingrese el DNI del cliente: ')
        diccionario_temporal['Nombre'] = input('Ingrese el nombre completo del cliente: ')
        diccionario_temporal['Direccion'] = input('Ingrese la direccón del cliente: ')
        diccionario_temporal['Telefono'] = input('Ingrese el número de télefono del cliente: ')
        diccionario_temporal['Mail'] = input('Ingrese el mail del cliente')
        preferencia = input('¿El cliente es preferente?: ')
        preferencia.upper()
        if preferencia == 'SI':
            diccionario_temporal['Preferente'] = True
        elif preferencia == 'NO':
            diccionario_temporal['Preferente'] = False
        clientes[DNI] = diccionario_temporal
        diccionario_temporal.clear()
    #Eliminar cliente
    elif condicion == 2:
        del clientes[input('Ingrese el DNI del cliente que desea eliminar: ')]
    #Mostrar cliente
    elif condicion == 3:
        cliente = int(input('Ingrese el DNI del cliente: '))
        
    #Listar clientes
        print('Lista de clientes')
        print('-----------------')
    elif condicion == 4:
    #Listar clientes preferentes
    elif condicion == 5:
        print('')
    
    print('1. Añadir cliente')
    print('2. Eliminar cliente')
    print('3. Mostrar cliente')
    print('4. Listar todos los clientes')
    print('5. Listar clientes preferentes')
    print('6. Terminar')
    condicion = int(input('Elija una opción: '))
