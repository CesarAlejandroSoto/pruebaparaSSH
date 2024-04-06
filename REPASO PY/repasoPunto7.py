'''7.	Una tienda tiene dos listas que contienen los ID de productos vendidos durante dos meses 
consecutivos. La tienda quiere saber cuantos productos se vendieron solo en el primer mes, cuantos 
productos se vendieron solo en el segundo mes y cuantos productos se vendieron en ambos meses, con el 
numero correspondiente de productos vendidos.
'''
print("Lista de los ids de los productos vendidos el primer mes : ");
Ids_mes1 = [1111,2222,3333,4444,5555,6666,7777,8888,9999,1010];
print(Ids_mes1);

print("Lista de los ids de los productos vendidos el primer mes : ");
Ids_mes2 = [1111,2222,5678,8765,9988,1234,4321,5555,6787,1010];
print(Ids_mes2);

print("Los id de los productos vendidios el primer mes son : ");
producto_mes1 = set(Ids_mes1);
print(producto_mes1);

print("Los id de los productos vendidios el segundo mes son : ");
producto_mes2 = set(Ids_mes2);
print(producto_mes2);

solo_mes1 = producto_mes1.difference(producto_mes2);
solo_mes2 = producto_mes2.difference(producto_mes1);
ambos_meses = producto_mes1.intersection(producto_mes2);

print("Los ids de los productos vendidos solo el primer mes son : ", solo_mes1);
print("Los ids de los productos vendidos solo el segundo mes son : ", solo_mes2);
print("Los ids de los productos vendidos en ambos meses : ", ambos_meses);

print("El numero de productos vendidos solo en el primer mes es : ", len(solo_mes1));
print("El numero de productos vendidos solo en el segundo mes es : ", len(solo_mes2));
print("El numero de productos vendidos en ambos meses es : ", len(ambos_meses));