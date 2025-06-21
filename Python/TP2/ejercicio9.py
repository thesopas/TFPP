# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus cliente. Lo ingredientes para 
# cada tipo de piza aparecen a continuación:
# Ingredientes vegetarianos: Pimientos y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. 
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta 
# le muestres el menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además 
# de la mozzarella y el tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la pizza 
# elegida es vegetariana o no y todos lo ingredientes que lleva.
eleccion = str(input('¿Desea una pizza vegetariana o no vegetariana: '))
if eleccion[0].upper() == 'N':
    print('Agregados:')
    print('  ')
    print('Peperoni')
    print('Jamón')
    print('Salmón')
    print('  ')
    agregados1 = str(input('Elija un agregado: '))
    print('Los ingredientes de la pizza son: tomate, mozzarella y ' , agregados1)
else:
    print('Agregados:')
    print('  ')
    print('Pimientos')
    print('Tofu')
    print('  ')
    agregados1 = str(input('Elija un agregado: '))
    print('Los ingredientes de la pizza son: tomate, mozzarella y ' , agregados1)