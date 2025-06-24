#
diccionario = {} #declara un diccionario vacío 
dl = {'Nombre': 'Daniel', 'Apellido': 'Dantur', 'Edad': 40} #declara un diccionario
# key:value {key1:value , key2:value , key3:value}
print(dl)

dl = dict(Nombre='Daniel', Apellido='Dantur', Edad=40) #otra forma de declarar un diccionario 
# se puede cambiar el valor de una key luego de haberla declarado
# key1=value , key2=value

dl = dict([('Nombre','Danie'),('Apellido','Dantur'),('Edad',40)]) #otra forma de declarar un diccionario 
#[(key1 , value) , (key2 , value)]
# Algunas propiedades 
# son dinamicos
# son idexados, tienen las keys pero no están ordenados
# pueden estar anidado (puede haber un diccionario dentro de otro)

d2 = {
    'Nombre completo' : {
        'Nombre' : 'Daniel',
        'Apellido': 'Dantur'
    },
    'Edad' : 40
} #Diccionario anidado
print(d2)


print(dl['Apellido']) #Obtiene el value de la key 
print(dl.get('Apellido'))
dl['Nombre'] = 'Miguel' #Modifica el value de una key
print(dl)
dl['Localidad'] = 'Las talitas' # Agrega una key con su value al diccionario 