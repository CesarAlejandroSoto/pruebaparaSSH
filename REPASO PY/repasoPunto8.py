'''8.	Se tiene un registro de ventas de una tienda y se quieren realizar varias operaciones utilizando 
diccionarios en Python. En este caso, se debe crear un diccionario que tenga como claves los nombres de los 
productos y como valores las cantidades vendidas. A partir de este diccionario, resolver lo siguiente:
•	Obtener el producto mas vendido y su cantidad.
•	Obtener el producto menos vendido y su cantidad.
•	Calcular el promedio de ventas de los productos.
•	Obtener la lista de productos en los que se vendieron más de 100 unidades.
'''

registro_ventas = {
    'producto1':50,
    'producto2':100,
    'producto3':150,
    'producto4':80,
    'producto5':110,
    'producto6':90
    }

cantidad_mas_vendido = max(registro_ventas, key = registro_ventas.get)
producto_mas_vendido = registro_ventas[cantidad_mas_vendido]
print("El producto mas vendido es ",cantidad_mas_vendido);
print("El producto mas vendido es ",producto_mas_vendido);
print(registro_ventas);

cantidad_menos_vendido = min(registro_ventas, key = registro_ventas.get)
producto_menos_vendido = registro_ventas[cantidad_menos_vendido]
print("El producto menos vendido es ",cantidad_menos_vendido);
print("El producto menos vendido es ",producto_menos_vendido);
print(registro_ventas);

print(registro_ventas.values());
len(registro_ventas);


promedio_ventas = sum(registro_ventas.values())/len(registro_ventas);
print("El promedio de ventas es : ",promedio_ventas);

productos_mas_vendidos = []

for producto, cantidad in registro_ventas.items():
    if cantidad > 100:
        productos_mas_vendidos.append(producto)
        
print("Los productos mas vendidos mayores a 100 : ", productos_mas_vendidos)