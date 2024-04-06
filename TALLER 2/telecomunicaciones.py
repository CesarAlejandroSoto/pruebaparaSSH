from numpy import *
from matplotlib.pyplot import *
import math


datos= array([2.5,3.2,4.1,2.9,3.5,4.3,4.6])

etiquetas= ["LUnes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

bar(etiquetas,datos)

xlabel("Dia de la semana")
ylabel("Uso de datos promedio(GB)")
title("Uso de datos promedio por dia de la semana")
show()

if mean(datos) > 4:
    print("Se deeb considerar ofrecer nuevos planes de datos.")
else:
    print("No es necesario ofrecer nuevos planes de datos.")