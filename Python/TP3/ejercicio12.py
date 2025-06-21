# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el
# número de veces que aparece la letra en la frase.
frase = str(input('Ingrese una frase: '))
letra = str(input('Ingrese una letra: '))
cantidad_a = 0
for i in frase:
    if i == letra:
        cantidad_a += 1 

print(cantidad_a)