electronica = {"TV","computadora","telefono"}
ropa = {"camisa","pantalon","zapato"}
alimentos = {"manzana","leche","pan"}

producto_vendido = "TV"
if producto_vendido in electronica:
    electronica.remove(producto_vendido)
elif producto_vendido in ropa:
    ropa.remove(producto_vendido)
elif producto_vendido in alimentos:
    alimentos.remove(producto_vendido)
else:
    print("producto no encontrado")

inventario_total = electronica.union(ropa,alimentos)
print("Productos totales:",inventario_total)

productos_comunes = electronica.intersection(ropa)
print("productos comunes entre electronica y ropa:",productos_comunes)