diccionario = {}
diccionario = {"python":1,"java":2,"javascript":3}
print(diccionario)

# mostrar el numero de elementos del diccionario
print("los elemntos del diccionario son:",len(diccionario))

# acceder a los valores de los elementos es con [clave]
print("el valor de la clave es :",diccionario["python"])

# insertar un elemento nuevo a mi diccionario es [clave]= #
diccionario["c++"]=4
print("nuevo elemento para mi diccionario",diccionario)

# para eliminar algun elemento del[clave]
del(diccionario["c++"])
print("elimino el elemento",diccionario)

# agregar una lista dentro de mi diccionario
diccionario["c/c++"]=[4,5]
print("nuevos elementos :",diccionario)

# agregar una tupla dentro de mi diccionario
diccionario["c/c++"]=(4,5)
print("nuevos elementos :",diccionario)

# agregar un conjunto dentro de mi diccionario
diccionario["otros"]={100,200,300}
print("nuevos elementos :",diccionario)

alumnos = {
    1:["cesar","soto"],
    2:["sara","soto"],
    3:["vanesa","archila"]
    }
if 1 in alumnos:
    print(alumnos[1])
else:
    print("Alumno 1 no existe")
if 2 in alumnos:
    print(alumnos[2])
else:
    print("Alumno 2 no existe")
if 3 in alumnos:
    print(alumnos[3])
else:
    print("Alumno 3 no existe")
if 4 in alumnos:
    print(alumnos[4])
else:
    print("Alumno 4 no existe")
    
# imprimir las claves del diccionario
print(alumnos.keys())

# imprimir los valores del diccionario
print(alumnos.values())

# imprimir los pares de las claves y valores del diccionario
print(alumnos.items())

# limpiar el diccionario
alumnos.clear()
print(alumnos)