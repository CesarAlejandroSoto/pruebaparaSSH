# los conjuntos no son ordenados y no se repiten elementos cuando se imprime
conjuntos = set() # conjunto vacio
conjuntos = {1,2,3,"a","b"}
print(conjuntos)

# para añadir un elemento al conjunto con add  y se añade al final
conjuntos.add(5)
print(conjuntos)

# para saber si un valor esta incluido en el conjunto
print(" el valor 3 esta en el conjunto?",3 in conjuntos)

# para eliminar un elemento en especifico 
conjuntos.discard(1)
print("eliminar el elemento 1 ",conjuntos)

a = {1,2,3}
b = {4,5,6,7}
c = {1,2,3,4,5,6,7}
d = {10,11,12}
#operaciones de conjuntos
print("la union de los conjuntos es", a.union(b))
print("la interseccion de los conjuntos es", a.intersection(b))
print("la diferencia de los conjuntos es", a.difference(b))
print("la diferencia simetrica de los conjuntos es", a.symmetric_difference(b))
print("los subconjuntos de los conjuntos es", a.issubset(c))
print("los superconjuntos de los conjuntos es", a.issuperset(c))
print("la disconexion lo que esta en a no esta en d de los conjuntos es", a.isdisjoint(d))

# para que un conjunto sea inmutable se hace de la siguiente manera
f = frozenset({53,6,4})
