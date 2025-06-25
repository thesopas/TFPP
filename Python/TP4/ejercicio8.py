# Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los
# elementos repetidos.
#entrada = str(input('Ingrese una palabra: '))
#print(entrada)
lista = []
lista2 = []
palabra = 'a'
while palabra != '':
    entrada = str(input('Ingrese una palabra para añadir a una lista: '))
    palabra = entrada
    if palabra != '':
        lista.append(entrada)
        lista2.append(entrada)
        print(lista)
print(lista)
print(lista2)
maximo = len(lista)
comparador = lista2[maximo - 1]
for i in range(maximo):
    if lista2[i] == comparador


