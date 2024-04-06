import math

class Materias:
  def __init__(self, num_opciones, num_requeridas):
    self.num_opciones = num_opciones
    self.num_requeridas = num_requeridas

  def num_combinaciones(self):
    return math.comb(self.num_opciones, self.num_requeridas)

class Estudiante:
  def __init__(self):
    self.contabilidad = Materias(6, 2)
    self.mercadotecnia = Materias(4, 2)
    self.informatica = Materias(3, 1)

  def num_formas_inscripcion(self):
    return self.contabilidad.num_combinaciones() * self.mercadotecnia.num_combinaciones() * self.informatica.num_combinaciones()

estudiante = Estudiante()
total_formas = estudiante.num_formas_inscripcion()
print("El número de formas posibles de inscripción es: ", total_formas)

class Materia:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    
    def combinaciones(self, n):
        if n > self.cantidad:
            return 0
        else:
            return self.factorial(self.cantidad) / (self.factorial(n) * self.factorial(self.cantidad - n))
    
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

contabilidad = Materia('Contabilidad', 6)
mercadotecnia = Materia('Mercadotecnia', 4)
informatica = Materia('Informática', 3)

total_combinaciones = contabilidad.combinaciones(2) * mercadotecnia.combinaciones(2) * informatica.combinaciones(1)

print(f"El número de formas en que se puede inscribir un estudiante en dos materias de contabilidad, dos de mercadotecnia y una de informática es: {total_combinaciones}")
