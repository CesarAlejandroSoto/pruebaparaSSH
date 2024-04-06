from itertools import *
import math
	
'''1. ¿De cuántas formas pueden colocarse los 11 jugadores de un equipo de fútbol
teniendo en cuenta que el portero no puede ocupar otra posición distinta que
la portería?'''
n = 11;
r = 10;
cantidad_permutaciones = 0;
formula_permutacion = math.factorial(n)/(math.factorial(n-r));
	
print(" el total de permutaciones son : ",formula_permutacion);
	
jugadores = permutations([1,2,3,4,5,6,7,8,9,10,11],10);
	
for elemento in list(jugadores):
	    
    print(elemento);
	    
    cantidad_permutaciones = cantidad_permutaciones + 1;
    
    
print(" el total de permutaciones son : ",cantidad_permutaciones);

