import math
'''3.	Un apostador tiene el presentimiento de que en la próxima jornada futbolística 
(en un torneo nacional con 28 equipos) ganarán 9 equipos en casa, empatarán 3 y ganarán en campo 
contrario (de visitantes) 2. ¿Cuántas apuestas deberá realizar para asegurarse un pleno de 14?'''
# Función para calcular el número de combinaciones de n elementos tomados k a la vez
def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Número total de resultados posibles de los 14 partidos
total_resultados = 3 ** 14

# Número de resultados posibles para cada uno de los 14 partidos seleccionados
resultados_posibles = 1
resultados_posibles *= comb(9, 9) * comb(19, 5) * comb(2, 0)
resultados_posibles *= 10 ** 5  # 5 partidos pueden ser empates o victorias del visitante

# Número mínimo de apuestas necesarias para asegurarse un pleno de 14
min_apuestas = math.ceil(total_resultados / resultados_posibles)

print("El número mínimo de apuestas necesarias es:", min_apuestas)
