"""El ejercicio 1 contiene en cada objeto de datos (Direccionamiento Abierto, Encadenamiento, Buckets) la implementación de la función
contar_comparaciones(), que devuelve la cantidad de comparaciones hecha por cada politica de manejo de colisiones. A continuación,
se detalla la implementación de dichas funciones."""

from ejercicio1 import TablaHashDirAbierto, TablaHashEncadenamiento, TablaHashBucket

def evaluar_tabla(tabla, claves_exito, claves_no_exito):
    for k in claves_exito:
        tabla.insertar(k)

    max_exito = 0
    min_exito = 9999
    for k in claves_exito:
        comp = tabla.contar_comparaciones(k)
        if comp > max_exito:
            max_exito = comp
        if comp < min_exito:
            min_exito = comp

    max_fallo = 0
    min_fallo = 9999
    for k in claves_no_exito:
        comp = tabla.contar_comparaciones(k)
        if comp > max_fallo:
            max_fallo = comp
        if comp < min_fallo:
            min_fallo = comp

    print("Máx búsqueda exitosa:", max_exito)
    print("Mín búsqueda exitosa:", min_exito)
    print("Máx búsqueda NO exitosa:", max_fallo)
    print("Mín búsqueda NO exitosa:", min_fallo)

if __name__ == "__main__":
    CLAVES_MUESTRA = [
            10429, 84512, 32901, 57183, 29405, 91827, 46290, 73819, 18294, 65043,
            39481, 82736, 50192, 27384, 94810, 61728, 38492, 70918, 15263, 49827,
            83746, 21903, 67482, 53910, 90281, 34817, 78192, 12094, 45671, 89102,
            23847, 60192, 74829, 31029, 95847, 48291, 19283, 84756, 52019, 37482,
            69182, 28374, 91028, 47586, 13920, 76483, 58291, 20394, 81920, 64738,
            39102, 72839, 16472, 59384, 92837, 41029, 85746, 29384, 63829, 51029,
            79482, 14829, 43920, 87291, 30192, 68473, 54920, 93847, 25483, 71029,
            17384, 49201, 86473, 35829, 62910, 57382, 98102, 24738, 75829, 11029,
            42837, 88392, 36472, 66192, 55829, 96473, 26384, 77291, 18392, 44829,
            80192, 33847, 61029, 56473, 97291, 22837, 73920, 15920, 46837, 83920
        ]
    CLAVES_NO_EXITOSAS = [
            10005, 20015, 30025, 40035, 50045, 60055, 70065, 80075, 90085, 12345,
            23456, 34567, 45678, 56789, 67890, 78901, 89012, 90123, 13579, 24680,
            11223, 22334, 33445, 44556, 55667, 66778, 77889, 88990, 99112, 10203
        ]

    N = len(CLAVES_MUESTRA)
    print("DIRECCIONAMIENTO ABIERTO: ")
    tabla_da = TablaHashDirAbierto(N)
    evaluar_tabla(tabla_da, CLAVES_MUESTRA, CLAVES_NO_EXITOSAS)

    print("ENCADENAMIENTO: ")
    tabla_encad = TablaHashEncadenamiento(N, 3)
    evaluar_tabla(tabla_encad, CLAVES_MUESTRA, CLAVES_NO_EXITOSAS)

    print("BUCKETS: ")
    tabla_bucket = TablaHashBucket(N, 4)
    evaluar_tabla(tabla_bucket, CLAVES_MUESTRA, CLAVES_NO_EXITOSAS)
