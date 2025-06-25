# Escribir un programa que almacene las asignaturas de una asignatura (por ejemplo Matemáticas, Física,
# Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio
# <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
asignatura = ['Matemáticas' , 'Física' , 'Química' , 'Historia' , 'Lengua']
print(len(asignatura))
mensaje = 'Yo estudio: ' + asignatura[0]
for i in range (1 , len(asignatura) - 1):
    mensaje = mensaje + ', Yo estudio: ' + asignatura[i]
mensaje = mensaje + ' y Yo estudio: ' + asignatura[-1]
print(mensaje)
