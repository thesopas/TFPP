compras = [] # Lista vacía

compras = ['pan', 'leche', 'huevos'] # Lista con elementos

print(compras) # Imprime la lista

item = compras[0]
print(item) # Imprime el primer elemento de la lista

compras.append('azúcar') # Añade un elemento al final de la lista
print(compras)

compras.insert(-2, 'sal') # Inserta un elemento en una posición específica
print(compras)

compras.sort()
print(compras) # Imprime la lista ordenada

compras.reverse()
print(compras) # Imprime la lista al revés

compras.remove('sal') # Elimina un elemento de la lista
print(compras) # Imprime la lista sin el elemento eliminado

compras.pop() # Elimina el último elemento de la lista
print(compras) # Imprime la lista sin el último elemento

compras.pop(1) # Elimina el elemento en la posición 1
print(compras) # Imprime la lista sin el elemento en la posición 1

compras.clear() # Elimina todos los elementos de la lista
print(compras) # Imprime la lista vacía

lista = ['uno', 2, 3.14, ['otra', 'lista']] # Lista mixta
print(lista) 
print(lista[3]) # Lista anidada
print(lista[3][0]) # Elemento de una lista anidada
print(type(lista[3])) # Es de tipo lista
lista[3].pop() # Puedo utilizar métodos de lista porque es una lista
print(lista[3]) # El pop anterior funcinó sin problemas

a = ['lavarropa', 'televisor', 'microondas']
b = a.copy() # Crea una copia 'superficial'
b.append('licuadora')
print(b)
print(a)

a[1] = 'DVD'
print(a)

c = ['computadora', 'parlante', 'teclado']
electro = a + c
print(electro)

print('DVD' in a)

print(list(range(0,101,2)))

todos_ceros = [0] * 10
print(todos_ceros)

lista_cadena = 'Este es un texto de ejemplo'.split()
print(lista_cadena)

d = a.copy()
print(id(a))
print(id(d))