tupla=(1,2,3,4,5,"a","b")
tupla[2]
# busca el elemento en la posicion que se le especifica
print("el elemento en la posicion 2 = ",tupla[2])
# toma las elemntos de la lista en el rango de las posiciones que se le piden
tupla[0:3]
print("los elementos entre la posicion 0 y 3",tupla[0:3])

# comprueba si el elemento en verdad esta en la tupla
print("el tres estara en la tupla ? ", 3 in tupla)

 # index busca la posicion del elemento que se le pide
print("el indice o posicion del elemento seleccionado es :", tupla.index(2))

# count busca o muestra cuantas veces se repite el elemento que se le da 
print("cuantas veces se repite el numero que selecciones: ", tupla.count(1))

# len me muestra la lingitud de la tupla
print("el tamaño de la tupla es :", len(tupla))

# convertir una tupla a lista
lista = list(tupla)
print(lista)
# convertir una lista a tupla
tupla2 = tuple(lista)
print(tupla2)
