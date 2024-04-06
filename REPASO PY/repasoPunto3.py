'''3.	Una persona desea llevar un registro de sus compras diarias y calcular sus gastos totales Para ello 
se utilizará la programación en Python. 
El programa debe permitir al usuario ingresar el nombre del producto y su precio. Estos datos se almacenarán,
y el programa calculara el gasto total sumando todos los precios de los productos. 
El programa también debe mostrar el gasto total y los productos comprados y permitir al usuario agregar mas 
productos a la lista o salir del programa. Para esto se utilizarán diferentes métodos de listas,
como append (), sum () y len (), etc.
'''

productos = [];
precios_productos = [];

numero_compras = int(input("Digite el numero de compras que hizo : "))
for i in range(numero_compras):
    
    producto = input("Ingrese el nombre del producto : ");
    precio_producto = float(input("Ingrese el precio del producto $: "));

    productos.append(producto);
    precios_productos.append(precio_producto);
    
   
print("Lista de productos comprados con su precio:")
print(productos);
print(precios_productos);

total_productos = sum(precios_productos);

print("El gasto total de la compra es de : $",total_productos);


