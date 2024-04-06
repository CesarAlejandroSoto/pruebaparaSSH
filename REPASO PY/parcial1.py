lista1=[];

numero=int(input("Digite la cantidad de numeros que desea agregar: "));
for posicion in range(numero):
    nuevo_numero=int(input("Digite un numero para agregar: "));
    lista1.append(nuevo_numero);
print(lista1);
print("Que accion desea hacer: ")
print("1. Añadir numero a la lista");
print("2. Añadir numero a la lista en una posicion especifica");
print("3. Longitud de la lista");
print("4. Eliminar el ultimo numero de la lista");
print("5. Contar valores de la lista");
print("6. Posición de un numero");
print("7. Mostrar numeros ");

accion=int(input("Digite el numero de la acción que desea realizar: "))

if accion == 1:
    nuevo_valor=int(input("Digite un numero para agregar: "));
    lista1.append(nuevo_valor);
    print(lista1);
elif accion == 2:
    valor_insertado=int(input("Digite la posición en la que desea insertar el nuevo valor: "));
    new_val=int(input("Digite el nuevo valor a insertar en la lista: "));
    lista1.insert(valor_insertado,new_val);
    print(lista1);
elif accion == 3:
    print("La longitud de la lista es: ", len(lista1));
elif accion == 4:
    lista1.pop();
    print(lista1);
elif accion == 5:
    lista1.count(lista1);
    print(lista1);
elif accion == 6:
    mostrar=int(input("Que numero desea saber su posicion? "));
    print("La posicion del numero es: ",lista1.index(mostrar));
elif accion == 7:
    print(lista1);
