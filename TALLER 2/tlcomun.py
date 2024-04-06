from numpy import *
from matplotlib.pyplot import *
import math

datos=array([]);
etiquetas=[];

cantidad=int(input("digite la cantidad de datos"));
for posicion in range(cantidad):
    valores_datos=float("digite el valor que desea agregar:");
    datos=append(datos,valores_datos);
    print(datos);
    nombres_etiquetas=str(input("digite el nombre de la etiqueta:"));
    etiquetas.append(nombres_etiquetas);
    print(etiquetas);

bar(etiquetas,datos);
xlabel("Dias");
ylabel("Datos");
title("Comparacion");
