# Registro de asistencia
asistencia = {
    "Juan": ["2022-03-01", "2022-03-03", "2022-03-05"],
    "María": ["2022-03-01", "2022-03-02", "2022-03-03", "2022-03-04", "2022-03-05"],
    "Pedro": ["2022-03-01", "2022-03-05"],
    "Luisa": ["2022-03-01", "2022-03-03", "2022-03-05"],
    "Ana": []
}

# Crear diccionario con las fechas de asistencia por estudiante
asistencia_por_estudiante = {}
for estudiante, fechas in asistencia.items():
    asistencia_por_estudiante[estudiante] = fechas

# Obtener lista de estudiantes que asistieron a todas las clases
asistieron_a_todas = []
for estudiante, fechas in asistencia_por_estudiante.items():
    if len(fechas) == len(asistencia):
        asistieron_a_todas.append(estudiante)

# Obtener lista de estudiantes que no asistieron a ninguna clase
no_asistieron = []
for estudiante, fechas in asistencia_por_estudiante.items():
    if len(fechas) == 0:
        no_asistieron.append(estudiante)

# Obtener lista de estudiantes que asistieron al menos a una clase
asistieron_al_menos_una = []
for estudiante, fechas in asistencia_por_estudiante.items():
    if len(fechas) > 0:
        asistieron_al_menos_una.append(estudiante)

# Calcular el porcentaje de asistencia de cada estudiante
porcentaje_asistencia = {}
for estudiante, fechas in asistencia_por_estudiante.items():
    porcentaje_asistencia[estudiante] = len(fechas) / len(asistencia) * 100

# Imprimir los resultados
print("Estudiantes que asistieron a todas las clases:", asistieron_a_todas)
print("Estudiantes que no asistieron a ninguna clase:", no_asistieron)
print("Estudiantes que asistieron al menos a una clase:", asistieron_al_menos_una)
print("Porcentaje de asistencia por estudiante:", porcentaje_asistencia)
