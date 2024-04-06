import itertools
'''1.	El candado de mi maleta tiene 7 posiciones en las que se puede poner cualquiera de los 10 dígitos
del 0 al 9. ¿Cuántas contraseñas diferentes podría poner? ¿Cuántas tienen todos sus números distintos? 
¿Cuántas tienen algún número repetido? ¿Cuántas tienen un número repetido dos veces?'''
# Cálculo del número de contraseñas posibles
num_combinaciones = 10 ** 7
print("Número de contraseñas posibles:", num_combinaciones)

# Cálculo del número de contraseñas con todos sus números distintos
num_permutaciones = 10 * 9 * 8 * 7 * 6 * 5 * 4
print("Número de contraseñas con todos sus números distintos:", num_permutaciones)

# Cálculo del número de contraseñas con algún número repetido
num_repetidos = num_combinaciones - num_permutaciones
print("Número de contraseñas con algún número repetido:", num_repetidos)

# Cálculo del número de contraseñas con un número repetido dos veces
num_2_repetidos = 10 * 9 * 8 * 7 * 6 * 5 * 1
print("Número de contraseñas con un número repetido dos veces:", num_2_repetidos)
