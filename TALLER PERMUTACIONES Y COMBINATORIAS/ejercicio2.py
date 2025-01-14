peso_paquetes = [];
paq_registrados = int(input("Digite la cantidad de paquetes que desea enviar:"));
for paquetes in range(paq_registrados):
    paq = int(input("Digite el peso de los paquetes: "));
    peso_paquetes.append(paq);
peso_paquetes.sort(reverse=True)  # sort weights in descending order

repartidores = [0]  # list of repartidores and their current load
for peso in peso_paquetes:
    opcion = False;
    for i, carga in enumerate(repartidores):
        if carga + peso <= 20:  # check if repartidor can carry package
            repartidores[i] += peso;
            opcion = True;
            break
    if not opcion:  # create new repartidor if none can carry package
        repartidores.append(peso);

num_repartidores = len(repartidores);
print(f"El numero de repartidores para hacer la entrega de los pedidos es de: {num_repartidores}");
