tienda_1 = set();

productos_normales_t1 = int(input("Digite la cantidad de productos normales que hay disponibles :"));

for posicion in range(productos_normales_t1):
    nombre = str(input("Digite el nombre del producto:"));
    tienda_1.add(nombre);
    
productos_exclusivos_t1 = int(input("Digite la cantidad de productos exclusivos:"));

for posicion in range(productos_exclusivos_t1):
    nombre = str(input("Digite el nombre del producto exclusivo:"));
    tienda_1.add(nombre);


tienda_2 = set();

productos_normales_t2 = int(input("Digite la cantidad de productos normales que hay disponibles :"));

for posicion in range(productos_normales_t2):
    nombre = str(input("Digite el nombre del producto:"));
    tienda_2.add(nombre);

productos_exclusivos_t2 = int(input("Digite la cantidad de productos exclusivos:"));

for posicion in range(productos_exclusivos_t2):
    nombre = str(input("Digite el nombre del producto exclusivo:"));
    tienda_2.add(nombre);

productos_comunes = tienda_1.intersection(tienda_2);
print("Los productos comunes entre las dos tiendas son:",productos_comunes);
comunes = len(productos_comunes);

productos_exclusivos = tienda_1.difference(tienda_2);
print("Los productos exclusivos de la tienda 1 son:",productos_exclusivos);
exclusivos_t1 = len(productos_exclusivos);

productos_exclusivos2 = tienda_2.difference(tienda_1);
print("Los productos exclusivos de la tienda 2 son:",productos_exclusivos);
exclusivos_t2 = len(productos_exclusivos_t2);

productos_ambas_tiendas = tienda_1.union(tienda_2)
print("Todos los productos de ambas tiendas:",productos_ambas_tiendas);
total_productos = len(productos_ambas_tiendas);
