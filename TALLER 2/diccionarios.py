from matplotlib.pyplot import *

ventas ={
    "Producto A": 75,
    "Producto B": 150,
    "Producto C": 50,
    "Producto D": 200,
    "Producto E": 125,
    "Producto F": 75,
}

productos_con_alta_demanda = set()

for producto, ventas in ventas.items():
    if ventas > 100:
        productos_con_alta_demanda.add(producto)
    elif ventas == 100:
        print(f"{producto} tuvo una demanda exctamente de 100 unidades")
    else:
        print(f"{producto} tuvo una demanda baja")

#productos = ventas.keys();
#unidades_vendidas = ventas.values()
#bar(productos, unidades_vendidas)
#xlabel("Productos")
#ylabel("Unidades vendidas")
#title("Datos de ventas de los ultimos seis meses")

print("Los siguientes productos tuvieron una demanda mayor a 100 unidades:")
for producto in productos_con_alta_demanda:
    print(producto)

#show()