'''9.	Se entrega un registro de asistencia de un curso y se deben realizar varias operaciones utilizando 
diccionarios en Python. Primero se creará el diccionario que tenga como claves los nombres de los 
estudiantes y como valores una lista con las fechas en que asistieron.
A partir de este diccionario resolver lo siguiente:
•	Obtener la lista de estudiantes que asistieron a todas las clases.
•	Obtener la lista de estudiantes que no asistieron a ninguna clase.
•	Obtener la lista de estudiantes que asistieron al menos a una clase.
•	Calcular el porcentaje de asistencia de cada estudiante.
'''

asistencia = {
    'cesar':['lunes','martes','miercoles'],
    'juli':['miercoles','jueves','viernes'],
    'dario':['lunes','martes','miercoles','jueves','viernes'],
    'sara':['martes','viernes'],
    'andrea':['lunes','martes','miercoles','jueves','viernes'],
    
    }



asistieron_a_todas = [estudiante for estudiante, lista in asistencia.items() if len(lista) == len(asistencia)]
print("Estudiantes que asistieron a todas las clases:", asistieron_a_todas)

# Obtener la lista de estudiantes que no asistieron a ninguna clase
no_asistieron = [estudiante for estudiante, lista in asistencia.items() if len(lista) == 0]
print("Estudiantes que no asistieron a ninguna clase:", no_asistieron)

# Obtener la lista de estudiantes que asistieron al menos a una clase
asistieron_al_menos_una = [estudiante for estudiante, lista in asistencia.items() if len(lista) > 0]
print("Estudiantes que asistieron al menos a una clase:", asistieron_al_menos_una)

# Calcular el porcentaje de asistencia de cada estudiante
porcentaje_asistencia = {estudiante: len(lista)/len(asistencia)*100 for estudiante, lista in asistencia.items()}
print("Porcentaje de asistencia de cada estudiante:", porcentaje_asistencia)

print(asistencia)