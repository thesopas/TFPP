# Escribir un programa que guarde en una variable un diccionario con diferentes divisas como
# {‘Peso’:’$’, ‘Dólar’:’US$’, ‘Euro’:’€’, ‘Yen’:’¥’}, pregunte al usuario por una divisa y
# muestre su símbolo o un mensaje indicando si la divisa no existe en el diccionario.
monedas = {'Peso':'$', 'Dólar':'US$', 'Euro':'€', 'Yen':'¥'}
divisas = input('Ingrese una divisa: ').capitalize()
#divisas.upper()
while divisas not in monedas:
    divisas = input('La divisa no pertenece al diccionario intente de nuevo: ').capitalize()
print(monedas[divisas])