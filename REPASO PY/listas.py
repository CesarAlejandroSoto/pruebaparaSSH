'''lista=[1,2,3,3,3,4,4,6,7,7]
print("primer elmento",lista[0]);
print("ultimo elemento",lista[-1]);
print("rango del primero al tercero",lista[0:3])
print("rango del primero al ultimo",lista[3:])'''

lista2= [1,1,2,3]
print(lista2);
# para saber la longitud de una lista
len(lista2);
print("len(lista)=",len(lista2));

# para añadir un elemento a la lista y se agrega al final de la lista
lista2.append(4)
print("lista2.append(4)=",lista2)

# para agregar un elemento en una posicion especifica
lista2.insert(0,3)
print("lista2.insert(0,3)=",lista2)

# para agregar mas de un elemento a la lista o mejor dicho otra lista a la lista
lista2.extend([5,6,7])
print("lista2.extend([5,6,7])=",lista2)

# es otra forma de hacer el paso anterior 
lista2= lista2+[8,9,10]
print("lista2= lista2+[8,9,10]=",lista2)


numero = int(input("digite un numero: "))
# uso in para denotar si el elemento esta incluido en la lista
if numero in lista2:
    print("el numero",numero, "esta en la lista")
else:
    print("el numero",numero,"no esta en la lista")

# para saber que valor esta en una posicion especifica
lista2.index(5)
print("el valor que esta en la posicion 5 es :",lista2.index(5))

#para saber cuantas veces se repite o esta un valor en la lista
lista2.count(1)
print("cuantas veces se repite el numero 1 en la lista:", lista2.count(1))

# elimina el ultimo valor de la lista
lista2.pop()
print("aca se elimina el ultimo elemento de la lista", lista2.pop())

# elimina el valor en la posicion que se le especifique
lista2.pop(0)
print("aca se elimina el primer elemento de la lista", lista2.pop(0))

# elimina el valor o elemento que se le pide
lista2.remove(5)
print("eliminar el numero 5", lista2)

# reordena los elementos desde el ultimo al primero
lista2.reverse()
print("reordena los elemntos de la lista desde el ultimo hasta el primero",lista2)

# ordena los elementos del mayor al menor
lista2.sort()
print("ordena los elementos de mayor a menor", lista2)

# elimina la lista
lista2.clear()
print(lista2)

print("Nota: en una lista si hay valores repetidos al momento\n de imprimirlos no me va a contar sino el elemento repetido")