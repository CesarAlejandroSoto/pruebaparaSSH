'''1.	Una persona necesita organizar su lista de tareas diarias en una lista 
en Python utilizando diferentes métodos de listas para agregar, eliminar y modificar tareas. 
El programa debe permitir al usuario ingresar una tarea y agregarla a la lista. 
Luego el usuario debe ser capaz de ver todas las tareas en la lista, 
eliminar una tarea especifica y marcar una tarea como completada.
Para lograr esto, se utilizarán diferentes métodos de listas, como append (), removed () y pop ().
'''

tareas_diarias = [];
numero_de_tareas = int(input("Digite la cantidad de tareas que realiza diariamente : "));
for tareas in range(numero_de_tareas):
    agregar_tareas = str(input(("Que tareas diarias va a realizar : ")));
    tareas_diarias.append(agregar_tareas);
print(tareas_diarias);

print("si le salio alguna otra tarea diga cuantas y cuales son : ")
tareas_nuevas = int(input("Digite la cantidad de acciones nuevas que quiere agregar : "));
for otra_tarea in range(tareas_nuevas):
    tareas_olvidadas = str(input("Si quiere hacer alguna otra tarea y desea agregarla especifique cual : "));
    tareas_diarias.append(tareas_olvidadas);

tareas_hechas = int(input("Digite la cantidad de tareas que ya cumplio : "))
for hechas in range(tareas_hechas):
    eliminar_tarea = str(input("si desea eliminar una tarea que ya haya cumplido especifique cual : "));
    tareas_diarias.remove(eliminar_tarea);


print("la lista de sus tareas diarias por cumplir  es : ")
print(tareas_diarias);