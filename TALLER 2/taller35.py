
usuario_ejemplo={};

cantidad_usuarios=int(input("digite cantidad de usuarios: "));

for elemento in range(cantidad_usuarios):
    nombre_usuario = str(input("ingrese el nombre del usuario:"));
    cantidad_generos = set();
    for genero in range(3):
        generos = str(input("Digite el genero musical:"));
        cantidad_generos.add(generos);
    usuario_ejemplo.setdefault(nombre_usuario,cantidad_generos);
    print(usuario_ejemplo);
