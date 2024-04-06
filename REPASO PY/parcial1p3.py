'''. Crear un programa que cree un diccionario simulando una cesta de la compra. El programa 
debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida 
terminar las compras. Después se debe mostrar por pantalla la lista de la compra y el total de 
la compra:'''

cesta={};
total = [];

for posicion in range(50):
    opcion = int(input("Desea añadir articulos a la cesta ? : 1. Si, 2. No : "));
    if opcion == 1:
        Articulo=str(input("Nombre del articulo: "));
        Precio=int(input("Precio del articulo: $"));
        total.append(Precio);
        cesta.setdefault(Articulo,Precio);
    elif opcion == 2:
        break
        
        
    
print(cesta);
print("El total a pagar es: ", sum(total));
