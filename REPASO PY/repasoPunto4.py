'''4.	Una tienda necesita gestionar su inventario y precios mediante un programa en Python, utilizando 
diferentes métodos como agregar, eliminar y modificar productos.
El programa debe permitir al usuario ingresar el nombre del producto, su precio y la cantidad de unidades 
en stock. Estos datos se almacenarán, y el programa permitirá agregar nuevos productos, modificar la cantidad 
de unidades en stock, eliminar productos y mostrar una lista actualizada del inventario.
'''

inventario = [];
i= int(input("Ingrese el numero de productos que quiere en su inventario : "))
for i in range(i):
    
    print("Nombre del producto precio y unidades : ")
    nombre_producto = str(input("Ingrese el nombre del producto: "));
    precio_producto = float(input("Ingrese el precio del producto: $"));
    unidades_stock = int(input("Ingrese el numero de unidades que hay en stock : "));
    productos = {nombre_producto:precio_producto};
    
    inventario.append(productos);
    inventario.append(unidades_stock);
print(inventario);


print("1. Modificar valores de stock : ");
print("2. Eliminar productos : ")
nuevos = int(input("que accion desea ejecutar : "));
if nuevos == 1:
    mod_und_stock = str(input("Digite el nombre del producto que cambio sus unidades de stock : "))
    print(inventario);
    indice = int(input("Ahora coloque el valor del indice en que esta ese valor a modificar : "))
    nuevo_valor = int(input("Digite el nuevo valor de las unidades en stock: "));
    inventario[indice] = nuevo_valor;
elif nuevos == 2:
    print("Digite la posicion del producto que desea eliminar : ");
    print(inventario);
    eliminar_producto = int(input("indice del producto que desea eliminar : "));
    inventario.pop(eliminar_producto);
    print(inventario);
    eliminar_stock = int(input("indice del stock del producto: "));
    inventario.pop(eliminar_stock);
print(inventario);