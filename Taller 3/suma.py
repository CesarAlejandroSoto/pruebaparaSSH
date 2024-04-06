# Definir una función que calcula la suma de los primeros n números
def suma_primeros(n):
  # Inicializar una variable para almacenar el resultado
  resultado = 0
  # Usar un bucle for para recorrer los números desde 1 hasta n
  for i in range(1, n + 1):
    # Sumar cada número al resultado
    resultado = resultado + i
  # Devolver el resultado
  return resultado

# Llamar a la función con el argumento 100 y mostrar el resultado
print(suma_primeros(100))