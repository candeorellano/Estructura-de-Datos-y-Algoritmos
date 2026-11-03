import numpy as np
import math

def es_primo(n):
    if n < 2:
        return False
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True

def obtener_primo(n):
    while not es_primo(n):
        n += 1
    return n

class TablaHashDirAbierto:
    __arreglo:np.ndarray
    __tamaño_M: int

    def __init__(self, N_claves):
        self.__tamaño_M = obtener_primo(int(N_claves / 0.7))
        self.__arreglo = np.empty(self.__tamaño_M, dtype=object)

    def getM(self):
        return self.__tamaño_M

    def insertar(self, k):
        pos = hash_division(k, self.__tamaño_M)
        i = 0

        while i < self.__tamaño_M and self.__arreglo[pos] is not None:
            if self.__arreglo[pos] == k:
                return # Ya existe la clave
            else:
                pos = (pos + 1) % self.__tamaño_M
                i += 1

        if i < self.__tamaño_M:
            self.__arreglo[pos] = k
        else:
            print("Tabla llena, no se puede insertar")

    def buscar(self, k):
        pos = hash_division(k, self.__tamaño_M)
        i = 0
        encontrado = False

        while i < self.__tamaño_M and self.__arreglo[pos] is not None and not encontrado:
            if self.__arreglo[pos] == k:
                encontrado = True
            else:
                pos = (pos + 1) % self.__tamaño_M
                i += 1

        if encontrado:
            return pos
        else:
            return -1 # Si no existe

    def contar_comparaciones(self, k: int):
        pos = hash_division(k, self.__tamaño_M)
        i = 0
        comparaciones = 0
        while i < self.__tamaño_M and self.__arreglo[pos] is not None:
            comparaciones += 1
            if self.__arreglo[pos] == k:
                return comparaciones
            pos = (pos + 1) % self.__tamaño_M
            i += 1
        # Si detuvo la búsqueda al encontrar una celda vacía (None), 
        # sumamos 1 por esa comparación que determinó que no está
        if i < self.__tamaño_M:
            comparaciones += 1
        return comparaciones

    def pertenece(self, k: int):
        pos = hash_division(k, self.__tamaño_M)
        i = 0
        while i < self.__tamaño_M and self.__arreglo[pos] is not None:
            if self.__arreglo[pos] == k:
                return True
            pos = (pos + 1) % self.__tamaño_M
            i += 1
        return False

    
#Objetos de Datos para definir el Objeto de Datos TablaHashEncadenamiento: Lista Enlazada y Nodo
class Nodo:
    __dato:int
    __sig:object

    def __init__(self, xdato = None):
        self.__dato = xdato
        self.__sig = None

    def getDato(self):
        return self.__dato

    def getSig(self):
        return self.__sig

    def setDato(self, xd):
        self.__dato = xd

    def setSig(self, xs):
        self.__sig = xs

class ListaEnlazada:
    __cab: Nodo
    __cant: int

    def __init__(self):
        self.__cab = None
        self.__cant = 0

    def getCabeza(self):
        return self.__cab

    def insertarCabeza(self, dato):
        # Insertar en la cabeza tiene costo O(1)
        nuevo = Nodo(dato)
        nuevo.setSig(self.__cab)
        self.__cab = nuevo
        self.__cant += 1

class TablaHashEncadenamiento:
    __arreglo: np.ndarray
    __tamaño_M:int

    def __init__(self, N_claves, cant_coli):
        self.__tamaño_M = obtener_primo(int(N_claves / cant_coli))
        self.__arreglo = np.empty(self.__tamaño_M, dtype=object)

        for i in range(self.__tamaño_M):
            self.__arreglo[i] = ListaEnlazada()

    def getM(self):
        return self.__tamaño_M

    def insertar(self, k):
        pos = hash_division(k, self.__tamaño_M)
        cab = self.__arreglo[pos].getCabeza()
        repetido = False

        while cab is not None and not repetido:
            if cab.getDato() == k:
                repetido = True
            else:
                cab = cab.getSig()

        if not repetido:
            self.__arreglo[pos].insertarCabeza(k)

    def buscar(self, k):
        pos = hash_division(k, self.__tamaño_M)
        cab = self.__arreglo[pos].getCabeza()
        encontrado = False

        while cab is not None and not encontrado:
            if cab.getDato() == k:
                encontrado = True
            else:
                cab = cab.getSig()

        if encontrado:
            return pos
        else:
            return -1 # no se encontro el elemento

    def contar_comparaciones(self, k:int):
        pos = hash_division(k, self.__tamaño_M)
        cab = self.__arreglo[pos].getCabeza()
        comparaciones = 0
        if cab is None:
            return 1  # 1 comparación al verificar que la cabeza es None
        while cab is not None:
            comparaciones += 1
            if cab.getDato() == k:
                return comparaciones
            cab = cab.getSig()
        return comparaciones

    def pertenece(self, k: int):
        pos = hash_division(k, self.__tamaño_M)
        i = 0
        while i < self.__tamaño_M and self.__arreglo[pos] is not None:
            if self.__arreglo[pos] == k:
                return True
            pos = (pos + 1) % self.__tamaño_M
            i += 1
        return False

class TablaHashBucket:
    __contadores: np.ndarray
    __matriz: np.ndarray
    __tamaño_M:int
    __tamaño_T:int
    __tam_bucket_b:int

    def __init__(self, N_claves, b):
        self.__tam_bucket_b = b

        # Área primaria: M = N / b (buscando el primo más cercano)
        self.__tamaño_M = obtener_primo(int(N_claves / b))

        # Tamaño total: T = M + 20% para el área de overflow
        self.__tamaño_T = int(self.__tamaño_M * 1.2)

        # Inicializamos la matriz de T x b vacía (con None)
        self.__matriz = np.empty((self.__tamaño_T, self.__tam_bucket_b), dtype=object)

        # Inicializamos los contadores de cada fila en 0
        self.__contadores = np.zeros(self.__tamaño_T, dtype=int)

    def getM(self):
        return self.__tamaño_M

    def insertar(self, k: int):
        fila = hash_division(k, self.__tamaño_M)
        col = self.__contadores[fila]
        insertado = False

        #Si hay lugar en el bloque del area Primaria
        if col < self.__tam_bucket_b:
            self.__matriz[fila][col] = k
            self.__contadores[fila] += 1
            insertado = True
        #Si no hay lugar, buscamos lugar en el area de OverFlow
        else:
            filaOverflow = self.__tamaño_M
            while not insertado and filaOverflow < self.__tamaño_T:
                colOverflow = self.__contadores[filaOverflow]
                if colOverflow < self.__tam_bucket_b:
                    self.__matriz[filaOverflow][colOverflow] = k
                    self.__contadores[filaOverflow] += 1
                    insertado = True
                else:
                    filaOverflow += 1

        if not insertado:
            print("Area de overflow llena. No se pudo insertar")

    def buscar(self, k):
        fila = hash_division(k, self.__tamaño_M)
        col = self.__contadores[fila]
        i = 0
        encontrado = False
        pos_encontrada = None

        #Busqueda en el Area Primaria
        while i < col and not encontrado:
            if self.__matriz[fila][i] == k:
                encontrado = True
                pos_encontrada = (fila, i)
            else:
                i += 1

        #Busqueda en el area de Overflow
        if col == self.__tam_bucket_b and not encontrado:
            filaOverflow = self.__tamaño_M
            while not encontrado and filaOverflow < self.__tamaño_T:
                colOverflow = self.__contadores[filaOverflow]
                j = 0
                while j < colOverflow and not encontrado:
                    if self.__matriz[filaOverflow][j] == k:
                        encontrado = True
                        pos_encontrada = (filaOverflow, j)
                    else:
                        j += 1
                filaOverflow += 1

        if not encontrado:
            print("Elemento no encontrado")
            return -1
        else:
            return pos_encontrada
        
    def contar_comparaciones(self, k:int):
        fila = hash_division(k, self.__tamaño_M)
        col = self.__contadores[fila]
        comparaciones = 0
        if col == 0:
            return 1  # 1 comparación al verificar que el bucket está vacío
        i = 0
        while i < col:
            comparaciones += 1
            if self.__matriz[fila][i] == k:
                return comparaciones
            i += 1
        if col == self.__tam_bucket_b:
            fila_ov = self.__tamaño_M
            while fila_ov < self.__tamaño_T:
                j = 0
                while j < self.__contadores[fila_ov]:
                    comparaciones += 1
                    if self.__matriz[fila_ov][j] == k:
                        return comparaciones
                    j += 1
                fila_ov += 1
        return comparaciones

    def pertenece(self, k: int):
        pos = hash_division(k, self.__tamaño_M)
        i = 0
        while i < self.__tamaño_M and self.__arreglo[pos] is not None:
            if self.__arreglo[pos] == k:
                return True
            pos = (pos + 1) % self.__tamaño_M
            i += 1
        return False


#Ejercicio 1.B) Funciones de transformacion
def hash_division(k: int, M: int):
    return k % M

def hash_extraccion(k: int, M: int):
    #Extraemos los dos ultimos digitos de forma matematica
    digitos = k % 100
    #Aplicamos modulo M por si el numero extraido es mayor o igual a M
    return digitos % M

def hash_plegado(k: int, M: int):
    acumulador = 0
    while k > 0:
        acumulador += k % 100 # Obtenemos y sumamos los últimos 2 dígitos
        k = k // 100 # Le quitamos esos últimos 2 dígitos a k
    return acumulador % M # Aplicamos módulo M al total

def hash_cuadradoMedio(k: int, M: int):
    cuadrado = k ** 2
    # 1. Dividimos entero por 1000 para sacar los últimos 3 dígitos
    sin_final = cuadrado // 1000
    # 2. Aplicamos mod 100 para quedarnos con los 2 dígitos que quedaron al final (los del medio)
    centrales = sin_final % 100
    # 3. Aplicamos módulo M
    return centrales % M

def hash_alfanumerico(k: int, M: int):
    acumulador = 0
    base = 10

    # Recorremos cada letra de la palabra junto con su posición (empezando desde 1)
    for i in range(len(k)):
        codigo_ascii = ord(k[i]) # Obtenemos el valor ASCII de la letra con la funcion ord
        peso = base ** (i + 1) # Calculamos 10^1, 10^2, 10^3...
        acumulador += codigo_ascii * peso # Multiplicamos y sumamos al total

    return acumulador % M # Ajustamos al tamaño M de la tabla

#Ejercicio 1.C) definir operaciones 'insertar' y 'buscar' (hechas en cada objeto de datos)