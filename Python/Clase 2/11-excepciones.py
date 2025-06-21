def leer_entero(mensaje='Ingrese un número: '):
    while True:
        try:
            return int(input(mensaje))
        except:
            print('Valor inválido')

def division():
    n = leer_entero()
    m = leer_entero()
    try:
        return n / m
    except (ZeroDivisionError):
        return float('inf')

print(division())
