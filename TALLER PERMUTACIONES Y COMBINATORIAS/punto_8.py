'''para elaborar el código de identificación de un producto se requiere un 
número de 20 dígitos que sea divisible entre 3 entre 10 y entre 4 y que además 
tenga 10 de sus dígitos iguales a uno cuál puede ser ese número'''


def generar_codigo():
    codigo = '1' * 10

    import random
    for i in range(10):
        codigo += str(random.randint(0, 9))

    if int(codigo) % 3 == 0 and int(codigo) % 10 == 0 and int(codigo) % 4 == 0:
        return codigo
    else:
        return generar_codigo()

codigo_producto = generar_codigo()
print(codigo_producto)
