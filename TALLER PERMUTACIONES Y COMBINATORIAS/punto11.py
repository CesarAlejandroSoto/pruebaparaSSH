from itertools import *
import math

''' Una empresa seleccionará su nuevo Comité, el cual estará integrado por 7 
miembros. Dentro de los elegibles se encuentran:
6 ingenieros
4 administradores
8 abogados
3 contadores
¿De cuántas formas puede integrarse el Comité si debe haber al menos 3 
Ingenieros, 1 Abogado, 2 Administradores y 1 Contador?'''


'''Ingenieros'''
cantidad_combinaciones = 0 ;
n=6;
r=3;
formula_combinatoria = math.factorial(n) / (math.factorial(r) * math.factorial(n - r));
print(" el total de combinaciones para los ingenieros son : ",formula_combinatoria);

ingenieros = combinations([1,2,3,4,5,6,],3);

for elemento in list(ingenieros):
    
    print(elemento);
    
    cantidad_combinaciones = cantidad_combinaciones + 1;
    
print("el total de combinaciones para los ingenieros es : ",cantidad_combinaciones);
ing = int(cantidad_combinaciones);

'''Abogados'''
cantidad_combinaciones = 0 ;
n=8;
r=1;
formula_combinatoria = math.factorial(n) / (math.factorial(r) * math.factorial(n - r));
print(" el total de combinaciones para los abogados son : ",formula_combinatoria);

abogados = combinations([1,2,3,4,5,6,7,8],1);

for elemento in list(abogados):
    
    print(elemento);
    
    cantidad_combinaciones = cantidad_combinaciones + 1;
    
print("el total de combinaciones para los abogados es : ",cantidad_combinaciones);
abo = int(cantidad_combinaciones);

'''Administradores'''
cantidad_combinaciones = 0 ;
n=4;
r=2;
formula_combinatoria = math.factorial(n) / (math.factorial(r) * math.factorial(n - r));
print(" el total de combinaciones para los administradores son : ",formula_combinatoria);

administradores = combinations([1,2,3,4,],2);

for elemento in list(administradores):
    
    print(elemento);
    
    cantidad_combinaciones = cantidad_combinaciones + 1;
    
print("el total de combinaciones para los administradores es : ",cantidad_combinaciones);
adm = int(cantidad_combinaciones);

'''Contadores'''
cantidad_combinaciones = 0 ;
n=3;
r=1;
formula_combinatoria = math.factorial(n) / (math.factorial(r) * math.factorial(n - r));
print(" el total de combinaciones para los contadores son : ",formula_combinatoria);

contadores = combinations([1,2,3,],1);

for elemento in list(contadores):
    
    print(elemento);
    
    cantidad_combinaciones = cantidad_combinaciones + 1;
    
print("el total de combinaciones para los contadores es : ",cantidad_combinaciones);
con = int(cantidad_combinaciones);


comite = ing*abo*adm*con;
print("La cantidad total de formas en que se puede integrar el comite es de : ",comite, "formas");