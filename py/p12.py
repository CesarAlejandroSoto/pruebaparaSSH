from itertools import *
import math

'''Víctor desea viajar de Medellín a España, pero debe ir a Rionegro y hacer escala 
en Portugal. Para ir de Portugal a España existen 6 líneas aéreas, para ir de 
Medellín a Rionegro lo puede hacer por vía terrestre en 3 rutas, o lo puede 
hacer por 2 rutas aéreas. Si para ir de Rionegro a Portugal existen 5 líneas 
aéreas. 
¿Cuántas maneras diferentes puede hacer el viaje Víctor? ¿cuántas maneras 
diferentes de ida y regreso?'''

'''Medellin-Rionegro: ruta terrestre'''
n = 3;
r = 1;
cantidad_permutaciones = 0;
formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones en la ruta Medellin-Rionegro_terrestre son : ",formula_permutacion);

primera_escala = permutations([1,2,3],1);

for elemento in list(primera_escala):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;

print(" el total de permutaciones en la ruta Medellin-Rionegro_terrestre son : ",cantidad_permutaciones);
Med_Rio1 = int(cantidad_permutaciones);

'''Medellin-Rionegro: ruta aerea'''

n = 2;
r = 1;
cantidad_permutaciones = 0;
formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones en la ruta Medellin-Rionegro_aerea son : ",formula_permutacion);

segunga_escala = permutations([1,2],1);

for elemento in list(segunga_escala):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;

print(" el total de permutaciones en la ruta Medellin-Rionegro_area son : ",cantidad_permutaciones);
Med_Rio2 = int(cantidad_permutaciones);

'''Rionegro-Portugal: ruta aerea'''

n = 5;
r = 1;
cantidad_permutaciones = 0;
formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones en la ruta Rionegro-Portugal_aerea son : ",formula_permutacion);

tercera_escala = permutations([1,2,3,4,5],1);

for elemento in list(tercera_escala):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;

print(" el total de permutaciones en la ruta Rionegro-Portugal_area son : ",cantidad_permutaciones);
Rio_Port = int(cantidad_permutaciones);

'''Portugal-España: Ruta aerea'''

n = 6;
r = 1;
cantidad_permutaciones = 0;
formula_permutacion = math.factorial(n)/(math.factorial(n-r));

print(" el total de permutaciones en la ruta Rionegro-Portugal_aerea son : ",formula_permutacion);

cuarta_escala = permutations([1,2,3,4,5,6],1);

for elemento in list(cuarta_escala):
    
    print(elemento);
    
    cantidad_permutaciones = cantidad_permutaciones + 1;

print(" el total de permutaciones en la ruta Rionegro-Portugal_area son : ",cantidad_permutaciones);
Port_Esp = int(cantidad_permutaciones);

'''¿Cuántas maneras diferentes puede hacer el viaje Víctor? ¿cuántas maneras 
diferentes de ida y regreso?'''

viaje_victor = Med_Rio1*Med_Rio2*Rio_Port*Port_Esp;
print("Las maneras diferentes en que victor puede hacer su viaje son : ",viaje_victor);
print("El anterior resultado son igualmente las veces de ida del viaje es decir : ",viaje_victor);
print(" El número de formas diferentes de ida y regreso se saca de multiplicar las 180 formas diferentes por sí mismas, ya que cada viaje de ida tiene una vuelta correspondiente. ");

ida_regreso = viaje_victor**2;
print("Las formas diferentes de ida y regreso son : ",ida_regreso,"formas");