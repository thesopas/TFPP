# Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los
# elementos repetidos.
#entrada = str(input('Ingrese una palabra: '))
#print(entrada)
palabras = []
palabras_sin_repetir = []
while True:
    palabra_nueva = input('Ingresá un palabra (vacía sin terminar): ')
    if palabra_nueva == '':
        break

    palabras.append(palabra_nueva)
for palabra in palabras:
    if palabra not in palabras_sin_repetir:
        palabras_sin_repetir.append(palabra)
print(palabras_sin_repetir)


