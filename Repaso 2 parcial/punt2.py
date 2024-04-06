import math

# Función para calcular la permutación de n objetos tomados de a r
def permutacion(n, r):
    return math.factorial(n) / math.factorial(n-r)

# Función para calcular la combinación de n objetos tomados de a r
def combinacion(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

# a) Seis comerciales diferentes
# Se deben seleccionar 6 comerciales de entre 6 opciones, ordenados
resultado_a = permutacion(6, 6)
print("El resultado para a) es:", resultado_a)

# b) Dos comerciales iguales y cuatro diferentes
# Se deben seleccionar 2 comerciales de entre 4 opciones diferentes y 1 de 2 opciones iguales, ordenados
resultado_b = permutacion(4, 2) * permutacion(2, 1)
print("El resultado para b) es:", resultado_b)

# c) Cuatro comerciales diferentes, uno debe aparecer 3 veces y los otros una sola vez
# El comercial que aparece 3 veces puede ser seleccionado de 4 opciones distintas, y se ordena en 3 posiciones
# El resto de comerciales se deben seleccionar de entre 3 opciones distintas y ordenarlos
resultado_c = 4 * permutacion(3, 3) * permutacion(3, 1) * permutacion(3, 1)
print("El resultado para c) es:", resultado_c)


import math

class DirectorTV:

    def __init__(self):
        pass

    def permutacion(self, n, r):
        return math.factorial(n) / math.factorial(n-r)

    def combinacion(self, n, r):
        return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

    def comerciales_diferentes(self):
        # Se deben seleccionar 6 comerciales de entre 6 opciones, ordenados
        return self.permutacion(6, 6)

    def comerciales_iguales(self):
        # Se deben seleccionar 2 comerciales de entre 4 opciones diferentes y 1 de 2 opciones iguales, ordenados
        return self.permutacion(4, 2) * self.permutacion(2, 1)

    def comerciales_mixtos(self):
        # El comercial que aparece 3 veces puede ser seleccionado de 4 opciones distintas, y se ordena en 3 posiciones
        # El resto de comerciales se deben seleccionar de entre 3 opciones distintas y ordenarlos
        return 4 * self.permutacion(3, 3) * self.permutacion(3, 1) * self.permutacion(3, 1)

directorTV = DirectorTV()

print("El resultado para a) es:", directorTV.comerciales_diferentes())

print("El resultado para b) es:", directorTV.comerciales_iguales())

print("El resultado para c) es:", directorTV.comerciales_mixtos())


