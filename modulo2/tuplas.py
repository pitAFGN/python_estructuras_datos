#tuplas dentro de una tupla
catologo = (
    ("Avatar", "James Cameron", 2011, 9.5),
    ("Five Nights At Freddys", "Emma Tammi", 2023, 7),
    ("Ready Play One", "Steven Spielberg", 2018, 9)
)

#Desempaquetado
for titulo, director, año, puntuacion in catologo:
    print(titulo, director, año, puntuacion)

#separador
ganador_oscar, *no_nominados = catologo
print("----------------------------------")
print("ganador del oscar: ", ganador_oscar)
print("no nominados al oscar", no_nominados)

#buscar por el director de la pelicula
def buscar_director (nombre_director):
    resultado = []

    for pelicula in catologo:
        if pelicula[1] == nombre_director:
            resultado.append(pelicula)
    return tuple(resultado)

#implementacion obtener estadisticas
def obtener_estadisticas ():
    puntuaciones = []

    for pelicula in catologo:
        puntuaciones.append(pelicula[3])
    minimo = min(puntuaciones)
    maximo = max(puntuaciones)
    promedio = sum (puntuaciones) / len(puntuaciones)

    return(minimo, maximo, promedio)

#desempaquetacion de obtener estadisticas
minimo, maximo, promedio = obtener_estadisticas()
print("----------------------------------")
print("Minimo: ", minimo)
print("Maximo: ", maximo)
print("Promedio: ", promedio)

print("----------------------------------")
resultado = buscar_director("James Cameron")
print(resultado)