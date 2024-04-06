'''6.Un profesor tiene una lista de las notas de sus estudiantes en diferentes asignaturas y quiere saber 
cuantos estudiantes obtuvieron al menos una nota sobresaliente (nota mayor o igual a 80) en ambas asignaturas. 
Cree un programa en Python que pida como entrada dos conjuntos que representen las notas de los estudiantes en 
cada asignatura y devuelva el numero de estudiantes que obtuvieron al menos una nota sobresaliente en ambas 
asignaturas'''

asignatura_1 = set();
asignatura_2 = set();

estudiantes = int(input("Digite la cantidad de estuadiantes del curso : "))
for e in range(estudiantes):
    nota1 = int(input("Digite la nota de la primera asignatura: "))
    asignatura_1.add(nota1);
    nota2 = int(input("Digite la nota de la segunda asignatura: "))
    asignatura_2.add(nota2);
    

notas_sobresalientes = asignatura_1.intersection(asignatura_2);

num_estudiantes_sobresalientes  = len([nota1 for nota1 in notas_sobresalientes if nota1 >= 80])

print({num_estudiantes_sobresalientes});

print("Notas de los estudiantes en la primera asignatura : ",asignatura_1);
print("Notas de los estudiantes en la segunda asignatura : ",asignatura_2);

print("Numero de estudiantes que sacaron almenos una nota sobresaliente :",len(asignatura_1.intersection(asignatura_2)),"estudiantes");
