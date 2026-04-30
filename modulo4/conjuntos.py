tienda_centro = {"Avatar", "Real Steal", "Ready Player One"}
tienda_sur = {"Kpop Demon Hunters", "GOAT", "Mario Bros La pelicula"}
tienda_norte = {"Matrix", "Duro De Follar", "Kpop Demon Hunters"}

#todas las peliculas
catologo_completo = tienda_centro.union(tienda_norte, tienda_sur)
#los que tienen peliculas en comun
Productos_comunes = tienda_norte.intersection(tienda_sur)
#los que no tienen cosas en comun con otras tiendas
exclusivos = tienda_centro.difference(tienda_sur)
#no tienen nada en comun
tienda_centro.isdisjoint(tienda_sur | tienda_norte)

#sets de usuarios con las categorias
usuario1 = {"Accion", "Suspenso"}
usuario2 = {"Drama", "Accion"}
usuario3 = {"Comedia", "Terror"}
#union
todos_los_generos = usuario1 | usuario2 | usuario3
#diferencias
solo_usuario1 = usuario1 - usuario2
#incluyendo
usuario1_con_usuario2 = usuario1 & usuario2
#Simetria
simetria = usuario1 ^ usuario2
#subcojuntos
usuario1 <= todos_los_generos

for pelicula in catologo_completo:
    print(pelicula)

print("Productos comunes:", Productos_comunes)
print("Exclusivos centro:", exclusivos)

print("Todos los géneros:", todos_los_generos)
print("Solo usuario1:", solo_usuario1)
print("Simetría:", simetria)
print("¿usuario1 es subconjunto?:", usuario1 <= todos_los_generos)