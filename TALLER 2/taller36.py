texto = " El gato es negro y blanco. El perro es marron y blanco. El raton es gris."

palabras = texto.split()

palabras_unicas = set(palabras)

frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print("Palabras unicas en el texto:")
for palabra in palabras_unicas:
    print(palabra, "----->",frecuencia_palabras[palabra])

palabras_comunes = set()
for palabra, frecuencia in frecuencia_palabras.items():
    if frecuencia == max(frecuencia_palabras.values()):
        palabras_comunes.add(palabra)

print("Las palabras mas comunes en el texto son:",palabras_comunes)
