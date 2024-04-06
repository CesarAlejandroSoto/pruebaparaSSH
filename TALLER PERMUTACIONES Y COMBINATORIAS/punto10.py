from itertools import *
import math

'''Calcular cuantas formas hay de acomodar los libros: Cuatro libros distintos 
de matemáticas, seis diferentes de física y dos diferentes de química se 
colocan en un estante.
De cuántas formas distintas es posible ordenarlos si:
• Los libros de cada asignatura deben estar todos juntos.
• Solamente los libros de matemáticas deben estar juntos.'''

'''• Los libros de cada asignatura deben estar todos juntos.'''
n = 3;
r = 3;

formula_permutacion1 = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones para las tres materias son : ",formula_permutacion1);

n = 4;
r = 4;

formula_permutacion2 = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones para los libros de matematicas son : ",formula_permutacion2);

n = 6;
r = 6;

formula_permutacion3 = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones para los libros de fisca son : ",formula_permutacion3);

n = 2;
r = 2;

formula_permutacion4 = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones para los libros de quimica son : ",formula_permutacion4);

print("Entonces para cuando todos los libros de cada asignatura deben estar juntos :  ");

estante = formula_permutacion1*formula_permutacion2*formula_permutacion3*formula_permutacion4;

print("El total de permutaciones seria de :  ", estante);

'''• Solamente los libros de matemáticas deben estar juntos.'''

n = 4;
r = 4;

formula_permutacion5 = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones para los libros de matematicas son : ",formula_permutacion5);

n = 8;
r = 8;

formula_permutacion6 = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones para los libros de fisica y quimica son : ",formula_permutacion6);


print("Entonces para cuando solo los libros de matematicas deben estar juntos : ");
solomat = formula_permutacion5*formula_permutacion6;
print("El total de permutaciones para cuando solo los de mates deben estar juntos es de : ",solomat);



'''• Los libros de cada asignatura deben estar todos juntos.'''
cantidad_permutaciones = 0;
materias = permutations(["Matematicas","Fisica","Quimica"],3);

for elemento in list(materias):
	    
    print(elemento);
	    
    cantidad_permutaciones = cantidad_permutaciones + 1;
    
print(" el total de permutaciones de las tres materias son : ",cantidad_permutaciones);
asig = int(cantidad_permutaciones);

cantidad_permutaciones = 0;
matematicas = permutations(["algebra","calculo","estadistica","geometria"],4);

for elemento in list(matematicas):
	    
    print(elemento);
	    
    cantidad_permutaciones = cantidad_permutaciones + 1;
    
print(" el total de permutaciones de los libros de matematicas  son : ",cantidad_permutaciones);
mat = int(cantidad_permutaciones);

cantidad_permutaciones = 0;
fisica = permutations(["vectores","dinamica","fuerza","trabajo","energia","circuitos"],6);
	
for elemento in list(fisica):
	    
    print(elemento);
	    
    cantidad_permutaciones = cantidad_permutaciones + 1;
    
    
print(" el total de permutaciones de los libros de fisica  son : ",cantidad_permutaciones);
fis = int(cantidad_permutaciones);

cantidad_permutaciones = 0;
quimica = permutations(["acidos","bases"],2);

for elemento in list(quimica):
	    
    print(elemento);
	    
    cantidad_permutaciones = cantidad_permutaciones + 1;
    
print(" el total de permutaciones de los libros de fisica  son : ",cantidad_permutaciones);  
quim = int(cantidad_permutaciones);


print("Entonces para cuando todos los libros de cada asignatura deben estar juntos :  ");
estante = asig*mat*fis*quim;
print("El total de permutaciones seria de : ", estante);

'''• Solamente los libros de matemáticas deben estar juntos.'''

cantidad_permutaciones = 0;
matematicas = permutations(["algebra","calculo","estadistica","geometria"],4);

for elemento in list(matematicas):
	    
    print(elemento);
	    
    cantidad_permutaciones = cantidad_permutaciones + 1;
    
print(" el total de permutaciones de los libros de matematicas  son : ",cantidad_permutaciones);
mat = int(cantidad_permutaciones);


cantidad_permutaciones = 0;
fis_quim = permutations(["vectores","dinamica","fuerza","trabajo","energia","circuitos","acidos","bases"],8);

for elemento in list(fis_quim):
	    
    print(elemento);
	    
    cantidad_permutaciones = cantidad_permutaciones + 1;
    
print(" el total de permutaciones de los libros de matematicas  son : ",cantidad_permutaciones);
fisic_quimic = int(cantidad_permutaciones);

print("Entonces para cuando solo los libros de matematicas deben estar juntos : ");
solomat = mat*fisic_quimic;
print("El total de permutaciones para cuando solo los de matematicas deben estar juntos es de : ",solomat);
