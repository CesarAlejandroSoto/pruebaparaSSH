from itertools import *
import math

''' Escribe un número de 10 dígitos que el primer dígito indique el número de 
ceros que hay en el número; el segundo dígito, el número de unos, y el tercer 
dígito el número de doces'''

lista =[];
for i in range(10):
    numero = int(input(("Escribe un numero  : ")));

    while numero>=0 and numero<=9:
        lista.append(numero);
print(lista);

n1 = lista[0];
n2 = lista[1];
n3 = lista[2];

lista =[0]*n1;
lista =[1]*n2;
lista =[2]*n3;
print(lista);
