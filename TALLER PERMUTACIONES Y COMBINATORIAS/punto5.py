from itertools import *
import math

'''. En una competencia participan 6 atletas, si se sabe que
solo se premia a los 3 primeros y que además no hay empate,
se sabe también que David que es uno de estos
6 atletas ha quedado primero. ¿De cuántas maneras
se podrá premiar a 3 de estos atletas?
'''

n = 5;
r = 2;
cantidad_permutaciones = 0;
formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones son : ",formula_permutacion);

print("David ha quedado en primer lugar, el podio puede entonces completarse con : ");
print(" Segundo   tercero")

atletas = permutations(["Cesar","Jorge","Brayan","Santiago","Sebastian"],2);

for elemento in list(atletas):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;
    
print("el total de permutaciones es : ",cantidad_permutaciones);