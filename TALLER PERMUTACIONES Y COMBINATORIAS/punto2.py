from itertools import *
import math

'''2. Una mesa presidencial está formada por ocho personas, ¿De cuántas formas
distintas se pueden sentar, si el presidente y el secretario siempre van juntos?'''

n = 8;
r = 6;
cantidad_permutaciones = 0;
formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones son : ",formula_permutacion);

personas = permutations([1,2,3,4,5,6,7,8],6);

for elemento in list(personas):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;

print(" el total de permutaciones son : ",cantidad_permutaciones);
