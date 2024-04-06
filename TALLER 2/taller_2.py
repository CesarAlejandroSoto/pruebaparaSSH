from numpy import *

agua=array([]);
produccion=array([]);

cantidad=int(input("digite la cantidad de datos:"));

for posicion in range(cantidad):
    dato_agua=int(input("digite un numero para agregar al array agua:"));
    agua=append(agua,dato_agua);
    print(agua);
    dato_produccion=int(input("digite un numero para agregar al array produccion:"));
    produccion=append(produccion,dato_produccion);
    print(produccion);

