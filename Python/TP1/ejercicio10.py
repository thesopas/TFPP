# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos
# ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu
# cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la
# cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
# la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
dinero_deposito = float(input('¿Cuánto dinero ingresará a su cuenta de ahorro?: '))
primer_año = dinero_deposito * 0.04 + dinero_deposito
dinero_deposito = primer_año
print('Sus ahorros en el primer año fueron: ' , dinero_deposito)
segundo_año = dinero_deposito * 0.04 + dinero_deposito
dinero_deposito = segundo_año
print('Sus ahorros en el segundo año fueron: ' , dinero_deposito)
tercer_año = dinero_deposito * 0.04 + dinero_deposito 
dinero_deposito = tercer_año
print('Sus ahorros en el segundo año fueron: ' , dinero_deposito)