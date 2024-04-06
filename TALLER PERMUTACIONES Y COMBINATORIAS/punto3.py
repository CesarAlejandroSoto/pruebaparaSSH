from itertools import *
import math

'''3. En una videoconferencia con 7 alumnos se requiere se conecten en forma
aleatoria a la videoconferencia.

¿De cuántas formas se pueden conectar si son libres de elegir el orden en que
deben conectarse?
'''
cantidad_combinaciones = 0 ;
n=7;
r=7;
formula_combinatoria = math.factorial(n) / (math.factorial(r) * math.factorial(n - r));
print(" el total de combinaciones son : ",formula_combinatoria);

alumnos = combinations([1,2,3,4,5,6,7],7);

for elemento in list(alumnos):
    
    print(elemento);
    
    cantidad_combinaciones = cantidad_combinaciones + 1;
    
print("el total de combinaciones es : ",cantidad_combinaciones);
