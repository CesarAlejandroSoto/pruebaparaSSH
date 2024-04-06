# Inventario de la tienda de electrónica
inventario = {}

# Función para agregar un nuevo producto al inventario
def agregar_producto(nombre, cantidad):
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad
    print("Producto agregado al inventario.")

# Función para eliminar un producto del inventario
def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado del inventario.")
    else:
        print("El producto no está en el inventario.")

# Función para actualizar la cantidad de un producto en el inventario
def actualizar_cantidad(nombre, cantidad):
    if nombre in inventario:
        inventario[nombre] = cantidad
        print("Cantidad actualizada en el inventario.")
    else:
        print("El producto no está en el inventario.")

# Menú de opciones para el usuario
while True:
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        agregar_producto(nombre, cantidad)
    elif opcion == "2":
        nombre = input("Nombre del producto: ")
        eliminar_producto(nombre)
    elif opcion == "3":
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        actualizar_cantidad(nombre, cantidad)
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")
