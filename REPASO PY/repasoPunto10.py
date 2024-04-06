'''
10.	Una tienda de electrónica necesita un programa de gestión de inventario para mantener un registro 
de sus productos y realizar un seguimiento de su stock. El programa debe permitir al usuario agregar 
nuevos productos, eliminar productos existentes y actualizar la cantidad de productos disponibles en el 
inventario.
'''

inventario = []

while True:
    print("Seleccione una opción:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad de producto")
    print("4. Mostrar inventario")
    print("5. Salir")
    opcion = input("Ingrese la opción: ")

    if opcion == "1":
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        producto = {"codigo": codigo, "nombre": nombre, "cantidad": cantidad}
        inventario.append(producto)
        print("Producto agregado al inventario")
    elif opcion == "2":
        codigo = input("Ingrese el código del producto a eliminar: ")
        for producto in inventario:
            if producto["codigo"] == codigo:
                inventario.remove(producto)
                print("Producto eliminado del inventario")
                break
        else:
            print("Producto no encontrado en el inventario")
    elif opcion == "3":
        codigo = input("Ingrese el código del producto a actualizar: ")
        cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        for producto in inventario:
            if producto["codigo"] == codigo:
                producto["cantidad"] = cantidad
                print("Cantidad del producto actualizada")
                break
        else:
            print("Producto no encontrado en el inventario")
    elif opcion == "4":
        print("Inventario:")
        for producto in inventario:
            print("Código:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Cantidad:", producto["cantidad"])
            print()
    elif opcion == "5":
        break
    else:
        print("Opción inválida")





