from itertools import *
import math

'''. un entrenador de fútbol quiere presentar una alineación con 3 defensas, 4 
centrocampistas y 3 delanteros. Si dispone de 3 porteros,7 defensas,10 
centrocampistas y 6 delanteros, ¿cuántas alineaciones distintas puede 
presentar teniendo en cuenta que cada jugador solo puede jugar en su línea
correspondiente?'''

'''Porteros'''
n = 3;
r = 1;
cantidad_permutaciones = 0;
formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones para los porteros es : ",formula_permutacion);

porteros = permutations([1,2,3],1);

for elemento in list(porteros):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;

print(" el total de permutaciones para los porteros es : ",cantidad_permutaciones);
por = int(cantidad_permutaciones);

'''Defensas'''
n = 7;
r = 3;
cantidad_permutaciones = 0;
formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones para los defensas es : ",formula_permutacion);

defensas = permutations([1,2,3,4,5,6,7],3);

for elemento in list(defensas):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;

print(" el total de permutaciones para los defensas es : ",cantidad_permutaciones);
defen = int(cantidad_permutaciones);

'''Centrocampistas'''
n = 10;
r = 4;
cantidad_permutaciones = 0;
formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones para los centrocampistas es : ",formula_permutacion);

defensas = permutations([1,2,3,4,5,6,7,8,9,10],4);

for elemento in list(defensas):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;

print(" el total de permutaciones para los centrocampistas es : ",cantidad_permutaciones);
cen = int(cantidad_permutaciones);

'''Delanteros'''
n = 6;
r = 3;
cantidad_permutaciones = 0;
formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones para los delanteros es : ",formula_permutacion);

defensas = permutations([1,2,3,4,5,6],3);

for elemento in list(defensas):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;

print(" el total de permutaciones para los delanteros es : ",cantidad_permutaciones);
dela = int(cantidad_permutaciones);

'''¿cuántas alineaciones distintas puede 
presentar teniendo en cuenta que cada jugador solo puede jugar en su línea
correspondiente?'''

alineaciones = por*defen*cen*dela;
print("El numero de alineaciones posibles es de : ",alineaciones);