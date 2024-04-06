disponible = set();

productos_disponibles = int(input("DSigite la cantidad de productos que hay disponibles :"));

for posicion in range(productos_disponibles):
    nombre = int(input("Digite el codigo del producto que esta disponible:"));
    disponible.add(nombre);

vendidos = set();

productos_vendidos = int(input("Digite la cantidad de productos vendidos:"));

for posicion in range(productos_vendidos):
    nombre = int(input("Digite el codigo del producto que ya han sido vendido:"));
    vendidos.add(nombre);

devuelto = set();

productos_devueltos = int(input("Digite la cantidad de productos devueltos:"));

for posicion in range(productos_devueltos):
    nombre = int(input("Digite el codigo del producto que ha sido devuelto:"));
    devuelto.add(nombre);

productos_disponibles_vendidos = disponible.union(vendidos);
print("Los productos que estan disponibles y vendidos en este momento son:",productos_disponibles_vendidos);
vendidos_disponibles = len(productos_disponibles_vendidos);

productos_han_devuelto_disponibles = devuelto.union(disponible);
print("Los productos que han sido devueltos y los disponibles hasta el momento son:",productos_han_devuelto_disponibles);
devueltos_disponibles = len(productos_han_devuelto_disponibles);

productos_disponibles_no_vendidos = disponible.difference(vendidos)
print("Los productos que estan disponibles pero no han sido vendidos hasta el momento son:",productos_disponibles_no_vendidos);
no_vendidos_disponibles = len(productos_disponibles_no_vendidos);



