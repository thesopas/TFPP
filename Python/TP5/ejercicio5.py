# Escribir un programa que almacene un diccionario con los créditos de las asignaturas de un curso
# {‘Matemática’:6, ‘Física’:4, ‘Química’:5} y después muestre por pantalla los créditos de
# cada asignatura en el formato <asignatura> tiene <creditos> créditos, donde
# <asignatura> es cada una de las asignaturas del curso <creditos> son sus créditos. Al final debe
# mostrar también el número total de créditos del curso.
materias = {'Matemática':6, 'Física':4, 'Química':5}
print(f"Matemática tiene {materias['Matemática']} créditos")
print(f"Física tiene {materias['Física']} créditos")
print(f"Química tiene {materias['Química']} créditos")
total = sum(materias.values())
print(f"El curso tiene un total de {total} créditos")