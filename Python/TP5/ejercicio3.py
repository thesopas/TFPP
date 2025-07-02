# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al
# usuario por una fruta, una cantidad en kilogramos y muestre por pantalla el precio de esa cantidad de la
# fruta seleccionada. Si la fruta no está en el diccionario, mostrar un mensaje informándolo.
precio_frutas = {'Banana':int(1990) , 'Manzana Roja':1890 , 'Naranja': 890 , 'Mandarina': 990 , 'Pera': 1690}
frutas = input('Ingrese una fruta:').capitalize()
while frutas not in precio_frutas:
    frutas = input('No tenemos esa fruta, intente con otra:').capitalize()
peso = int(input('¿Cuántos kilos quiere?: '))
precio = precio_frutas[frutas] * peso
print('El precio por esa cantidad de fruta es $' , precio)