"""Se implemento el metodo pertenece() en los Objetos de datos (DA, Encad, Bucket). Ver el Ejercicio 1
En este caso, usaremos la tabla Hash Direccionamiento Abierto"""

import random
from ejercicio1 import TablaHashDirAbierto

def encontrar_duplicados(datos: list):
    tabla = TablaHashDirAbierto(len(datos))
    duplicados = []

    for k in datos:
        if tabla.pertenece(k):
            if k not in duplicados:
                duplicados.append(k)
        else:
            tabla.insertar(k)

    return duplicados

if __name__ == "__main__":
    random.seed(42)
    # Generamos un conjunto grande de 1200 datos (con valores entre 1000 y 1800 para que haya repetidos)
    conjunto_datos = [random.randint(1000, 1800) for _ in range(1200)]

    repetidos = encontrar_duplicados(conjunto_datos)
    print("Cantidad de datos analizados:", len(conjunto_datos))
    print("Cantidad de elementos duplicados encontrados:", len(repetidos))
    print("Primeros 15 duplicados:", repetidos[:15])
