from itertools import *
import math

'''El comité escolar (presidente, secretario y tesorero) se eligen entre 12 
maestros, sin importar si es hombre o mujer. ¿De cuantas maneras puede 
integrarse el comité? '''


n = 12;
r = 3;
cantidad_permutaciones = 0;
formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones son : ",formula_permutacion);


docentes = permutations([1,2,3,4,5,6,7,8,9,10,11,12],3);
	
for elemento in list(docentes):
	    
    print(elemento);
	    
    cantidad_permutaciones = cantidad_permutaciones + 1;
    
    
print(" el total de permutaciones son : ",cantidad_permutaciones);
