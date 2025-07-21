# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las
# palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción>
# separados por comas (por ejemplo: ’hola:hello,adiós:goodbye,gracias:thanks’). El
# programa creará el diccionario de palabras y sus traducciones, y lo mostrará en pantalla con un formato
# como el siguiente:
# Diccionario Español-Inglés
# --------------------------
# hola: hello
# adiós: goodbye
# gracias: thanks

traducciones_d = {}

traducciones_s = input('Entrada: ')
traducciones_l = traducciones_s.split(',')
traducciones_t = tuple(traducciones_l)

for i in range(len(traducciones_t)):
    lista = traducciones_t[i].split(':')
    traducciones_d[lista[0]] = lista[1]
    
print('Diccionario Español-Inglés')
print('--------------------------')
for j in traducciones_d:
    print(j , ': ' , traducciones_d[j])
