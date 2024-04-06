usuarios = {
    "usuario1": {"rock","pop","jazz"},
    "usuario2": {"rock","indie","electronica"},
    "usuario3": {"pop","jazz","hip hop"},
    "usuario4": {"rock","indie","folk"}
}
generos_todos_usuarios = set()
for usuario in usuarios:
    generos_todos_usuarios = generos_todos_usuarios.union(usuarios[usuario])

print("Generos mas populares", generos_todos_usuarios)

