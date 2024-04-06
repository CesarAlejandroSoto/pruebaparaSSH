def assign_packages(packages, capacity):
    # Sort packages by decreasing weight
    packages = sorted(packages, reverse=True)

    # Initialize the list of repartidores and the index of the current repartidor
    repartidores = [[]]
    current_repartidor = 0

    # Assign packages to repartidores
    for package in packages:
        # If the current repartidor has enough capacity, add the package to the list
        if sum(repartidores[current_repartidor]) + package <= capacity:
            repartidores[current_repartidor].append(package)
        # If the current repartidor is full, create a new repartidor and add the package to its list
        else:
            current_repartidor += 1
            repartidores.append([package])
    
    # Return the number of repartidores and the list of packages assigned to each repartidor
    return len(repartidores), repartidores

packages = [5, 3, 7, 2, 4, 1, 6]
capacity = 20

num_repartidores, repartidores = assign_packages(packages, capacity)
print("Number of repartidores:", num_repartidores)
for i, repartidor in enumerate(repartidores):
    print("Repartidor", i+1, "packages:", repartidor)
