tup = ('uno', 2, 3.14) # las tuplas puede tener valors mixtos
print(tup)

item = tup[1] # la tupla tiene sus elementos ordenados
print(item)

tup2 = ('algo',) # tupla de un sólo elemento
print(type(tup2))

def registracion() -> tuple:
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    edad = int(input('Ingrese su edad: '))

    return nombre, apellido, edad

# print(type(registracion())) # <class 'tuple'>
# nombre, apellido, edad = registracion()
nombre, apellido, edad = ('Daniel', 'Dantur', '40')
print(nombre)
print(apellido)
print(edad)