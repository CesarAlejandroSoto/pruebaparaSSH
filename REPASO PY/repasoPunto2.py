'''2.	Una empresa desea realizar un análisis de los resultados de una encuesta que ha realizado entre sus
clientes. La encuesta consistió en preguntar a los clientes sobre su experiencia con el servicio que ofrece 
la empresa. Cada cliente pudo dar una puntuación del 1 al 5 siendo 1 la puntuación mas baja y 5 la puntuación 
más alta.

La empresa desea obtener las siguientes estadísticas a partir de los resultados de la encuesta.
•	La puntuación media obtenida de la encuesta.
•	El porcentaje de clientes que han dado una puntuación de 4 o 5.
•	El porcentaje de clientes que han dado una puntuación de 1 o 2.
Escribe un programa en Python que solicite al usuario que introduzca las puntuaciones de cada uno de los 
clientes encuestados. El programa deberá almacenar las puntuaciones en una lista y utilizar diferentes 
métodos de la lista para realizar los cálculos estadísticos necesarios.
'''

puntuacion_de_satisfaccion = [];

clientes = int(input("Ingrese la cantidad de clientes que fueron encuestados : "));

for clnts in range(clientes):
    print("El rango de satisfaccion es de 1 a 5 : 1 siendo malo y 5 siendo muy bueno")
    satisfaccion = int(input("Digite su satisfaccion con el servicio : "))
    puntuacion_de_satisfaccion.append(satisfaccion);
print("Puntuaciones de satisfaccion de algunos clientes : ")
print(puntuacion_de_satisfaccion);

print("La cantidad de clientes encuestados es de : ", clientes);

suma = sum(puntuacion_de_satisfaccion);

print("El promedio de satisfaccion de los clientes es de : " ,suma/clientes);


clientes_stf_buena = sum(satisfaccion >= 4 for satisfaccion in puntuacion_de_satisfaccion);

print("El porcentaje de clientes que han dado una puntuación de 4 o 5 :");
porcentaje_stf_buena = clientes_stf_buena/len(puntuacion_de_satisfaccion ) * 100;
print(porcentaje_stf_buena);

clientes_stf_mala = sum(satisfaccion <=2 for satisfaccion in puntuacion_de_satisfaccion);

print("El porcentaje de clientes que han dado una puntuación de 1 o 2 :");
porcentaje_stf_mala = clientes_stf_mala/len(puntuacion_de_satisfaccion ) * 100;
print(porcentaje_stf_mala);
