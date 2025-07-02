# Escribir un programa que pida la fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha
# en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
meses = {'1':'Enero','2':'Febrero','3':'Marzo','4':'Abril','5':'Mayo',
         '6':'Junio','7':'Julio','8':'Agosto','9':'Septiembre',
         '10':'Octubre','11':'Nobiembre','12':'Diciembre'}
fecha = input('Ingrese una fecha:')
lista = fecha.split('/')
print(lista[0] , ' de ' , meses[lista[1]] , ' de ' , lista[2])
