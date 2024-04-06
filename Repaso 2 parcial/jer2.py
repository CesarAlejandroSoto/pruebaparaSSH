import math
'''2.	Un gato se encuentra en A y un ratón en B. El gato avanza de centro de casilla en centro de
casilla moviéndose hacia la derecha o hacia abajo, nunca retrocede. ¿Cuántos caminos distintos puede
recorrer el gato para cazar al ratón?'''
def num_caminos(m, n):
    return math.comb(m + n, m)

m = 3  # número de casillas hacia la derecha
n = 4  # número de casillas hacia abajo
print("Número de caminos distintos:", num_caminos(m, n))
