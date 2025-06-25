# Escribir un programa que almacene las asignaturas de una asignatura (por ejemplo Matemáticas, Física,
# Química, Historia y Lengua) en una lista, pregunte al usuario la nota que obtuvo en cada asignatura, y
# después las muestre por pantalla con el mensaje En <asignatura> sacaste <nota> donde
# <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
# notas introducidas por el usuario.
asignatura = ['Matemáticas' , 'Física' , 'Química' , 'Historia' , 'Lengua']
mensaje = ''
for i in range(len(asignatura)):
    nota = str(input('¿Qué nota obtuvo en ' + asignatura[i] + '?: '))
    mensaje = mensaje + ' En ' + asignatura[i] + ' sacaste ' + nota + ', '
print(mensaje)
