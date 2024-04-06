python = set();

alumnos_python = int(input("La cantidad de estudiantes que se inscribieron en python  es:"));

for posicion in range(alumnos_python):
    nombre = str(input("Digite el nombre:"));
    python.add(nombre);


java = set();

alumnos_java = int(input("La cantidad de estudiantes que se inscribieron a java es:"));

for posicion in range(alumnos_java):
    nombre = str(input("Digite el nombre:"));
    java.add(nombre);


inscritos_ambos_cursos = python.intersection(java);
print("Los estudiantes que se inscribieron a ambos cursos fueron:",inscritos_ambos_cursos);
ambos_cursos = len(inscritos_ambos_cursos);

inscritos_python = python.difference(java);
print("Los estudiantes que solo se inscribieron a python fueron:",inscritos_python);
cantidadc = len(inscritos_python);

inscritos_java = java.difference(python);
print("Los estudiantes que solo se inscribieron a java fueron:",inscritos_java);
cantidadcf = len(inscritos_java);
