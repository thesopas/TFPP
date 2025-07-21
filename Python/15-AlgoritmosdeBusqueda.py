#Busqueda lineal: se analiza elemento por elemento 
#Busqueda binaria: se parte la lista en dos, pero la lista tiene que estar ordenada. Se analiza el elemento del medio 
#para ver si es el elemento buscado, si no lo es se pregunta si el elemento es mayor o menor al buscado, en base a eso 
#se procede a repetir el proceso en la mitad de la lista que corresponde. Este proceso es mucho más eficiente ya 
#que se realizan menos preguntas. 
#Métodos de ordenamiento
#Bubble sort: compara elemento a elemento y se van ordenando
#selection sort: selecciona el primer elemento y va comparandolo con todos los elementos restantes, si alguno es menor
#este los reemplaza y continua el camino; y así sucesivamente. Una vez llega al final lleva el menor elemento econtrado
#al principio de la lista y repite el proceso si tener en cuenta al primero.
#Insertion sort: buscar
#Sheel sort:
#Merge sort:


def busqueda_lineal(lista, objetivo):
    for indice in range(len(lista)):
        if lista[indice]==objetivo:
            return indice
    return None

def busqueda_binaria(lista, objetivo, inicio, fin):
    if inicio > fin:
        return None
    centro = (inicio + fin)//2
    if lista[centro]==objetivo:
        return centro
    elif lista[centro]<objetivo:
        return busqueda_binaria(lista, objetivo,centro+1,fin)
    else:
        return busqueda_binaria(lista,objetivo,inicio,centro-1)

#Bubble sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                #swap i needed
                lista[j], lista[j+1] = lista[j+1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista

#Selection sort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
        return lista
    
#Instertion sort
def insertion_sor(lista):
    n = len(lista)
    for i in range(1, n):
        item = lista[i]
        j = j - 1
        while j >= 0 and lista[j] > item:
            lista[j + 1] = lista[j]
            j -= 1
        lista[i + j] = item
    return lista

#Shell sort
def shell_sort(lista):
    n = len(lista)
    salto = n//2
    while salto > 0:
        for i in range(salto, n):
            temp = lista[i]
            j = i 
            while j >= salto and lista[j - salto] > temp:
                lista[j] = lista[j - salto]
                j -= salto
            lista[j] = temp 
    
#Merge sort
def merge_sort(lista):
    if len(lista) > 1:
        centro = len(lista)//2
        izquierda = lista[:centro]
        derecha = lista[centro:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

#Quick sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista)//2]
        izquierda = [x for x in lista if x < pivot]
        derercha = [x for x in lista if x > pivot]
        return quick_sort(izquierda) + [pivot] + quick_sort(derercha)
