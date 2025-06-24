# conjunto se define con una llave {}
conjunto = {1, 3, 5, 7, 7, 5}
#un conjunto no almacena duplicados
#No se puede acceder a los elementos individualmente porque no están ordenados 
conjutno2 = {1, 'dos', }
#se pueden poner varios tipos de datos dentro de un conunto
#los conjutos solo aceptan elementos inmutables (que no varíen), ose que un set no puede ir dentro de un set
conjunto = set(['uno', 'dos', 'tres'])
#se puede convertir una lista en conjunto siempre que los elementos sean inmutables
#una lista dentro de una lista no se puede convertir en conjunto
for elemento in conjunto:
    print(elemento)
#los conjuntos son iterables 
print('uno' in conjunto)
#se puede verificar si un elemento es parte de un conjunto

conjunto.add('cuatro') #agrega un elemento al conjunto
print(conjunto)
conjunto.remove('dos') #elimina un elemento del conjunto (aunque no exista dentro del conjunto (error))
conjunto.discard('dos') #elimina un elemento del conjunto pero no cae en el error del remove
conjunto.pop() #elimina un elemento al azar del conjunto
conjunto.clear() #elimina todos los elementos del set
#cuando se eliminan todos elementos en consola se muestra como set() porque {} están reservados para los 
#diccionarios
conjunto = set() #declara un set vacío 

#otros tipos de conjunto

frozen = frozenset(1, 2, 3) #declaro un frozenset
print(frozen)
#convierte a un conjunto en inmutable
#se puede usar para agregar un conjunto dentro de otro conjunto)