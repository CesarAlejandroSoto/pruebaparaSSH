# Registro de asistencia
asistencia = {
    "Juan": ["2022-01-01", "2022-01-08", "2022-01-15", "2022-01-22", "2022-01-29"],
    "María": ["2022-01-01", "2022-01-08", "2022-01-22", "2022-01-29"],
    "Pedro": ["2022-01-01", "2022-01-08", "2022-01-15", "2022-01-22"],
    "Luisa": ["2022-01-01", "2022-01-22", "2022-01-29"]
}

# Obtener la lista de estudiantes que asistieron a todas las clases
asistieron_todas = [estudiante for estudiante, lista in asistencia.items() if len(lista) == len(asistencia)]
print("Estudiantes que asistieron a todas las clases:", asistieron_todas)

# Obtener la lista de estudiantes que no asistieron a ninguna clase
no_asistieron = [estudiante for estudiante, lista in asistencia.items() if len(lista) == 0]
print("Estudiantes que no asistieron a ninguna clase:", no_asistieron)

# Obtener la lista de estudiantes que asistieron al menos a una clase
asistieron_al_menos_una = [estudiante for estudiante, lista in asistencia.items() if len(lista) > 0]
print("Estudiantes que asistieron al menos a una clase:", asistieron_al_menos_una)

# Calcular el porcentaje de asistencia de cada estudiante
porcentaje_asistencia = {estudiante: len(lista)/len(asistencia)*100 for estudiante, lista in asistencia.items()}
print("Porcentaje de asistencia de cada estudiante:", porcentaje_asistencia)
