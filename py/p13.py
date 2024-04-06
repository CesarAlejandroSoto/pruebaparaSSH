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
cantidad_combinaciones = 0;
formula_combinatoria = math.factorial(n) / (math.factorial(r) * math.factorial(n - r));

print(" el total de permutaciones para los porteros es : ",formula_combinatoria);

porteros = combinations([1,2,3],1);

for elemento in list(porteros):
    
    print(elemento);
    
    cantidad_combinaciones = cantidad_combinaciones + 1;

print(" el total de permutaciones para los porteros es : ",cantidad_combinaciones);
por = int(cantidad_combinaciones);

'''Defensas'''
n = 7;
r = 3;
cantidad_combinaciones = 0;
formula_combinatoria = math.factorial(n) / (math.factorial(r) * math.factorial(n - r));

print(" el total de permutaciones para los defensas es : ",formula_combinatoria);

defensas = combinations([1,2,3,4,5,6,7],3);

for elemento in list(defensas):
    
    print(elemento);
    
    cantidad_combinaciones = cantidad_combinaciones + 1;

print(" el total de permutaciones para los defensas es : ",cantidad_combinaciones);
defen = int(cantidad_combinaciones);

'''Centrocampistas'''
n = 10;
r = 4;
cantidad_combinaciones = 0;
formula_combinatoria = math.factorial(n) / (math.factorial(r) * math.factorial(n - r));

print(" el total de permutaciones para los centrocampistas es : ",formula_combinatoria);

defensas = combinations([1,2,3,4,5,6,7,8,9,10],4);

for elemento in list(defensas):
    
    print(elemento);
    
    cantidad_combinaciones = cantidad_combinaciones + 1;

print(" el total de permutaciones para los centrocampistas es : ",cantidad_combinaciones);
cen = int(cantidad_combinaciones);

'''Delanteros'''
n = 6;
r = 3;
cantidad_combinaciones = 0;
formula_combinatoria = math.factorial(n) / (math.factorial(r) * math.factorial(n - r));

print(" el total de permutaciones para los delanteros es : ",formula_combinatoria);

defensas = combinations([1,2,3,4,5,6],3);

for elemento in list(defensas):
    
    print(elemento);
    
    cantidad_combinaciones = cantidad_combinaciones + 1;

print(" el total de permutaciones para los delanteros es : ",cantidad_combinaciones);
dela = int(cantidad_combinaciones);

'''¿cuántas alineaciones distintas puede 
presentar teniendo en cuenta que cada jugador solo puede jugar en su línea
correspondiente?'''

alineaciones = por*defen*cen*dela;
print("El numero de alineaciones posibles es de : ",alineaciones);