import math

# Función para calcular el número de combinaciones de n elementos tomados k a la vez
def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Número de formas de inscribirse en dos materias de contabilidad
contabilidad = comb(6, 2)

# Número de formas de inscribirse en dos materias de mercadotecnia
mercadotecnia = comb(4, 2)

# Número de formas de inscribirse en una materia de informática
informatica = comb(3, 1)

# Número total de formas de inscribirse en las materias
total = contabilidad * mercadotecnia * informatica

print("El número de formas de inscribirse es:", total)

class Materias:
    def __init__(self, contabilidad, mercadotecnia, informatica):
        self.contabilidad = contabilidad
        self.mercadotecnia = mercadotecnia
        self.informatica = informatica

    def calcular_combinaciones(self):
        # Calculamos todas las posibles combinaciones de materias
        combinaciones_contabilidad = self.calcular_combinaciones_materias(self.contabilidad, 2)
        combinaciones_mercadotecnia = self.calcular_combinaciones_materias(self.mercadotecnia, 2)
        combinaciones_informatica = self.calcular_combinaciones_materias(self.informatica, 1)
        # Calculamos el número total de combinaciones posibles
        total_combinaciones = len(combinaciones_contabilidad) * len(combinaciones_mercadotecnia) * len(combinaciones_informatica)
        # Retornamos el resultado
        return total_combinaciones

    def calcular_combinaciones_materias(self, materias, num_materias):
        # Calculamos todas las posibles combinaciones de un conjunto de materias
        from itertools import combinations
        return list(combinations(materias, num_materias))

# Definimos las materias
contabilidad = ['Materia 1', 'Materia 2', 'Materia 3', 'Materia 4', 'Materia 5', 'Materia 6']
mercadotecnia = ['Materia 7', 'Materia 8', 'Materia 9', 'Materia 10']
informatica = ['Materia 11', 'Materia 12', 'Materia 13']

# Creamos una instancia de la clase Materias y calculamos las combinaciones posibles
materias = Materias(contabilidad, mercadotecnia, informatica)
combinaciones_posibles = materias.calcular_combinaciones()

# Mostramos el resultado
print(f"El número de formas en las que un estudiante puede inscribirse es {combinaciones_posibles}")


class Materias:
    def __init__(self, contabilidad, mercadotecnia, informatica):
        self.contabilidad = contabilidad
        self.mercadotecnia = mercadotecnia
        self.informatica = informatica

    def combinaciones(self):
        c = self.combinaciones_k(self.contabilidad, 2)
        m = self.combinaciones_k(self.mercadotecnia, 2)
        i = self.combinaciones_k(self.informatica, 1)
        return c * m * i

    @staticmethod
    def combinaciones_k(n, k):
        if n < k:
            return 0
        else:
            return Materias.factorial(n) // (Materias.factorial(k) * Materias.factorial(n - k))

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * Materias.factorial(n - 1)


m = Materias(6, 4, 3)
print(m.combinaciones())  # Output: 540
