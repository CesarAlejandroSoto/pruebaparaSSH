# Crear dos listas vacías para almacenar los nombres y precios de los productos
nombres_productos = []
precios_productos = []

# Variable para mantener el registro del número de productos comprados
num_productos = 0

# Bucle for para solicitar al usuario los nombres y precios de los productos
for i in range(1, 100):
    # Solicitar al usuario el nombre del producto y su precio
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Ingrese el precio del producto: "))

    # Agregar el nombre y precio del producto a las listas correspondientes
    nombres_productos.append(nombre_producto)
    precios_productos.append(precio_producto)

    # Actualizar el número de productos comprados
    num_productos += 1

    # Solicitar al usuario si desea agregar más productos o salir del programa
    opcion = input("¿Desea agregar otro producto? (s/n): ")
    if opcion == 'n':
        break

# Calcular el gasto total sumando todos los precios de la lista de precios
gasto_total = sum(precios_productos)

# Mostrar al usuario la lista de productos comprados y el gasto total
print("Lista de productos comprados:")
for i in range(num_productos):
    print(f"{nombres_productos[i]}: ${precios_productos[i]}")
print(f"Gasto total: ${gasto_total}")