# Escribir un programa que cree un diccionario simulando un carrito de compras. El programa debe pedir
# el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se
# debe mostrar por pantalla la lista de artículos y el precio total, con un formato como el siguiente:
productos = {}
condicion = ''
condicion = condicion.upper()
articulo = input('Ingrese un producto: ')
precio = int(input('Ingrese su precio: '))
productos[articulo] = precio

while True:
    condicion = input('Desea ingresar más productos: ')
    condicion = condicion.upper()
    if condicion == 'NO':
        break
    articulo = input('Ingrese un producto: ')
    precio = int(input('Ingrese su precio: '))
    productos[articulo] = precio

print('Lista de compras')
print('---------------')
for i in range(len(productos)):
    print()

#se puede iterar sobre los keys y lo values 


