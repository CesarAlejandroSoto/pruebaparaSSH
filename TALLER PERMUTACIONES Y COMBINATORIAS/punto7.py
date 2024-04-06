from itertools import *
import math

''' Escribe un número de 10 dígitos que el primer dígito indique el número de 
ceros que hay en el número; el segundo dígito, el número de unos, y el tercer 
dígito el número de doces'''

lista =[];
for i in range(10):
    numero = int(input(("Escribe un numero  : ")));

    while numero>=0 and numero>=9:
        lista.append(numero);
print(lista);

n1 = lista[0];
n2 = lista[1];
n3 = lista[2];

lista =[0]*n1;
lista =[1]*n2;
lista =[2]*n3;
    
n = 3;
r = 3;

formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de ceros es : ",formula_permutacion);


n = 2;
r = 2;

formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de unos es : ",formula_permutacion);

n = 1;
r = 1;

formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de dos es : ",formula_permutacion);


    
cantidad_permutaciones = 0;

personas = permutations([6,2,1,0,0,0,1,0,0,0][4:10],1);

for elemento in list(personas):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;
    
print("El numero de ceros es  : ",cantidad_permutaciones);

cantidad_permutaciones = 0;

personas = permutations([6,2,1,0,0,0,1,0,0,0][:2],1);

for elemento in list(personas):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;
    
print("El numero de unos es  : ",cantidad_permutaciones);

cantidad_permutaciones = 0;

personas = permutations([6,2,1,0,0,0,1,0,0,0][2:3],1);

for elemento in list(personas):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;
    
print("El numero de dos es  : ",cantidad_permutaciones);


