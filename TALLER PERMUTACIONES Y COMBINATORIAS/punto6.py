from itertools import *
import math

''' Debemos ordenar 7 personas distintas (Ana, Luis, Juan, Ely, Luz, Cris y Tavo) 
en tres asientos. ¿Cuántos ordenamientos distintos se pueden obtener?
¿Cuántos ordenamientos tiene a Ely en la primera posición?
¿Cuántos tendrá a Ely en la 1ra posición y a Luis en la tercera?
¿En cuántos estarán Ana o Cris?'''

n = 7;
r = 3;
cantidad_permutaciones1 = 0;

formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones son : ",formula_permutacion);


personas = permutations(["Ana", "Luis", "Juan", "Ely", "Luz", "Cris", "Tavo"],3);

for elemento in list(personas):
    
    print(elemento);
    
    cantidad_permutaciones1 = cantidad_permutaciones1+ 1;
    
print("el total de permutaciones es : ",cantidad_permutaciones1);

'''pregunta numero dos'''

cantidad_permutaciones2 = 0;
print("Dejo a Ely ubicada en la primera posicion asi que la quito de la lista : ");
personas = permutations(["Ana", "Luis", "Juan", "Luz", "Cris", "Tavo"],2);

for elemento in list(personas):
    
    print(elemento);
    
    cantidad_permutaciones2 = cantidad_permutaciones2 + 1;
    
print("Los ordenamientos que tiene ely en la primera posicion son  : ",cantidad_permutaciones2);

'''pregunta numero tres'''
cantidad_permutaciones3 = 0;
print("Dejo a Ely ubicada en la primera posicion y a Luis en la tercera asi que los quito de la lista : ");
personas = permutations(["Ana", "Juan", "Luz", "Cris", "Tavo"],1);

for elemento in list(personas):
    
    print(elemento);
    
    cantidad_permutaciones3 = cantidad_permutaciones3 + 1;
    
print("Los ordenamientos que tiene ely en la primera posicion y a luis en la tercera son  : ",cantidad_permutaciones3);


'''pregunta numero cuatro'''
cantidad_permutaciones4 = 0;
print("La veces en las que Ana o Cris no estarian seria quitarlos de la lista :")
personas = permutations(["Luis", "Juan", "Ely", "Luz", "Tavo"],3);

for elemento in list(personas):
    
    print(elemento);
    
    cantidad_permutaciones4 = cantidad_permutaciones4 + 1;
    
print("Los ordenamientos en los que Ana o Cris no estarian son  : ",cantidad_permutaciones4);

print("Entonces el numero de veces en los que Ana o Cris estan presentes seria :");
print("Restar el total de ordenaminetos menos los ordenaminetos en los que Ana o Cris no estan : ");
print("El resultado seria : ",cantidad_permutaciones1-cantidad_permutaciones4);

