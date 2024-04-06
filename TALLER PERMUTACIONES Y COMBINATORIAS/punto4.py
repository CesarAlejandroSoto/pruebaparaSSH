from itertools import *
import math


'''4. Una empresa quiere crear un código de tres letras seguidas de tres números
para etiquetar sus productos ¿cuántos códigos puede crear si decide utilizar
los 10 números y las 26 letras del abecedario y no se pueden repetir ni letras ni
números?
'''
n=26
r=3
formula_permutacion1 = math.factorial(n)/(math.factorial(n-r));
print(" el total de permutaciones del abecedario son : ",formula_permutacion1);

cantidad_permutaciones = 0;
n=10
r=3
formula_permutacion2 = math.factorial(n)/(math.factorial(n-r));
print(" el total de permutaciones de los numeros  son : ",formula_permutacion2);

permutacion = formula_permutacion1*formula_permutacion2
print(" el total de permutaciones son : ",permutacion);

numeros = [0,1,2,3,4,5,6,7,8,9];
abecedario = ["a","b","c","d","e","f","g","h","i""j","k","l","m","n","ñ","p","o","q","r","s","t","u","v","w","x","y","z"]

abc= list(permutations(abecedario,3));
num = list(permutations(numeros,3));


print(abc);
print(num);


codigos = len(abc) * len(num) ;
print("el numero de permutaciones posibles es de :", codigos);

total_codigos = zip(abc,num);
cod = list(total_codigos);
print("Los codigos quedarian de la siguiente manera : ", cod);



