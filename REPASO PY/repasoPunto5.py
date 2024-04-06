'''5.	Dado un conjunto de frutas y un conjunto de vegetales, cree una función en Python que devuelva un 
nuevo conjunto que contenga todos los elementos de ambos conjuntos sin elementos duplicados.'''


'''print("Conjunto de frutas : ")
frutas = {"manzana","naranja","fresa","mango","banano","durazno"};
print("Conjunto de vegetales : ")
vegetales = {"cebolla","lechuga","pepino","habichuela","cilantro"};

print("Conjunto que contiene a todos los elementos: ")
fruits_and_vegetables = {print(frutas.union(vegetales))}'''


def union_set(frutas, vegetales):
    return frutas.union(vegetales)

frutas = {"manzana","naranja","fresa","mango","banano","durazno"};

vegetales = {"cebolla","lechuga","pepino","habichuela","cilantro"};

print("Conjunto que contiene a todos los elementos : ");
nuevo_conjunto = union_set(frutas, vegetales)
print(nuevo_conjunto)

