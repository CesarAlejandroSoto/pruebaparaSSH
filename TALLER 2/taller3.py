conciertos = set();

usuarios = int(input("La cantidad de personas que asistieron al concierto  es:"));

for posicion in range(usuarios):
    nombre = str(input("Digite el nombre:"));
    conciertos.add(nombre);



conferencias = set();

asistentes = int(input("La cantidada de asistentes a la conferencia es:"));

for posicion in range(asistentes):
    nombre = str(input("Digite el nombre:"));
    conferencias.add(nombre);



asistentes_ambos_eventos = conciertos.intersection(conferencias);
print("Los asistentes a ambos eventos fueron:",asistentes_ambos_eventos);
cantidadccf = len(asistentes_ambos_eventos);


solo_concierto = conciertos.difference(conferencias);
print("Los asistentes solo al concierto fueron:",solo_concierto);
cantidadc = len(solo_concierto);

solo_conferencia = conferencias.difference(conciertos);
print("Los asistentes solo a la conferencia fueron:",solo_conferencia);
cantidadcf = len(solo_conferencia);
