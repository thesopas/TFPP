try:
    monto = int(input('Ingrese dinero: '))
except:
    raise ValueError('El monto dede ser entero')