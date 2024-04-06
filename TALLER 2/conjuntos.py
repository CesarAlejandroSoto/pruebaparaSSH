conjunto_vacio = set();

elementos =int(input("Digite cuantos elementos agregara:"));

for posicion in range(elementos):
    datos=int(input("Digite el numero que va agregar al conjunto:"));
    conjunto_vacio.add(datos);

print(conjunto_vacio);
#conjunto_vacio.remove(2);
conjunto_vacio.pop();
