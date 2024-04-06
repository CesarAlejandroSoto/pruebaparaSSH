from itertools import *
import math

'''El comité escolar (presidente, secretario y tesorero) se eligen entre 12 
maestros, sin importar si es hombre o mujer. ¿De cuantas maneras puede 
integrarse el comité? '''

cantidad_combinaciones = 0 ;
n=12;
r=3;
formula_combinatoria = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
print(" el total de combinaciones son : ",formula_combinatoria);

docentes = combinations([1,2,3,4,5,6,7,8,9,10,11,12],3);

for elemento in list(docentes):
    
    print(elemento);
    
    cantidad_combinaciones = cantidad_combinaciones + 1;
    
print("el total de combinaciones es : ",cantidad_combinaciones);