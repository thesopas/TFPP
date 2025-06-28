# Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los
# elementos repetidos.
#entrada = str(input('Ingrese una palabra: '))
#print(entrada)
lista = []
lista2 = []
lista3 = []
lista4 = []
palabra = 'a'
while palabra != '':
    entrada = str(input('Ingrese una palabra para añadir a una lista: '))
    palabra = entrada
    if palabra != '':
        lista.append(entrada)
        lista2.append(entrada)
        lista3.append(entrada)
        print(lista)
#print(lista)
#print(lista2)
#print(lista3)
maximo = len(lista)
for i in range(1 , maximo):
    if lista[i] == lista2[i]:
        lista4.append(lista.index(lista[i]))
print(lista)
print(lista2)
print(lista3)
print(lista4)

