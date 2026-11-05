# DIGRAFOS

import numpy as np

class DigrafoSecuencial:
    __cantVertices: int
    __matriz: np.ndarray

    def __init__(self, xvert):
        self.__cantVertices = xvert
        self.__matriz = np.zeros((self.__cantVertices, self.__cantVertices), dtype=int)

    def getCantVertices(self):
        return self.__cantVertices

    def agregarArista(self, u, v):
        self.__matriz[u,v] = 1 #solo marcamos una 'direccion'

    def adyacentes(self, u):
        listaVecinos = []

        for v in range(self.__cantVertices):
            if self.__matriz[u, v] == 1:
                listaVecinos.append(v)
        return listaVecinos

    def rea(self, s):
        d = [float('inf')] * self.__cantVertices
        cola = [s]
        d[s] = 0

        while len(cola) > 0:
            v = cola.pop(0)

            for u in self.adyacentes(v):
                if d[u] == float('inf'):
                    d[u] = d[v] + 1
                    cola.append(u)
        return d

    def camino(self, u, v):
        distancias = self.rea(u)
        return distancias[v] != float('inf')

    def aciclico(self):
        # Estados: 0 (No Visitado), 1 (En proceso de exploración), 2 (Totalmente explorado)
        d = [0] * self.__cantVertices

        for s in range(self.__cantVertices):
            if d[s] == 0:
                if self.detectarCicloDG(s, d):
                    return False
        return True

    def detectarCicloDG(self, s, d):
        d[s] = 1 # en proceso

        for u in self.adyacentes(s):
            if d[u] == 0:
                if self.detectarCicloDG(u, d):
                    return True
            elif d[u] == 1:
                return True

        d[s] = 2 #totalmente explorado
        return False

    def conexoFuerte(self):
        # 1. Probamos iniciar el recorrido desde CADA vértice
        for s in range(self.__cantVertices):
            distancias = self.rea(s)

            # 2. Revisamos si quedó algún nodo inalcanzable desde 's'
            for d in distancias:
                if d == float('inf'):
                    return False # No es fuertemente conexo
        return True # Todos pueden llegar a todos

    ##Operaciones exclusivas de DIGRAFO

    def gradSalida(self, u):
        return len(self.adyacentes(u)) #devuelve la cantidad de aristas que 'salen' del nodo u

    def gradEntrada(self, u):
        cont = 0

        for v in range(self.__cantVertices):
            if self.__matriz[v, u] == 1:
                cont += 1

        return cont #devuelve la cantidad de aristas que 'entran' al nodo u

    def nodo_fuente(self, u):
        # Es fuente si no le llegan aristas (entrada=0), pero sí salen de él (salida>0)
        return self.grad_entrada(u) == 0 and self.grad_salida(u) > 0

    def nodo_sumidero(self, u):
        # Es sumidero si le llegan aristas (entrada>0), pero no sale ninguna (salida=0)
        return self.grad_entrada(u) > 0 and self.grad_salida(u) == 0

    # Mas operaciones y algoritmos

    def ordenTopologico(self):
        marca = [False] * self.__cantVertices
        resultado = []
        
        for v in range(self.__cantVertices):
            if marca[v] == False:
                self._topologicVisita(v, marca, resultado)
                
        # En este algoritmo basado en REP, el orden correcto se obtiene al invertir la lista final
        return resultado[::-1]

    def _topologicoVisita(self, v, marca, resultado):
        marca[v] = True # 1. Marcamos el vértice actual como VISITADO

        for w in self.adyacentes(v): # 2. Recorremos sus adyacentes
            if marca[w] == False: # Si el vecino NO ha sido visitado, lo visitamos recursivamente
                self._topologicoVisita(w, marca, resultado)

        resultado.append(v) # 3. Al terminar de explorar todas sus ramas, lo guardamos en el resultado

    def dijkstra(self, origen):
        # 1. Inicialización de la Tabla (T)
        conocido = [False] * self.__cantVertices
        distancia = [float('inf')] * self.__cantVertices
        camino = [None] * self.__cantVertices
        
        distancia[origen] = 0
        
        # Para i desde 1 hasta |V| hacer...
        for _ in range(self.__cantVertices):
            
            # v <- vértice con la distancia más corta y desconocido
            v = -1
            min_dist = float('inf')
            for i in range(self.__cantVertices):
                if conocido[i] == False and distancia[i] < min_dist:
                    min_dist = distancia[i]
                    v = i
                    
            # Si no quedan vértices alcanzables, cortamos la función y devolvemos lo que tenemos
            if v == -1:
                return distancia, camino
                
            # T[v].conocido <- True
            conocido[v] = True
            
            # Para cada w adyacente a v hacer
            for w in self.adyacentes(v):
                peso = self.__matriz[v, w] # Asumimos que la matriz ahora guarda los costos
                
                # Si T[w].conocido = False
                if conocido[w] == False:
                    # Si T[v].distancia + w(v,w) < T[w].distancia
                    if distancia[v] + peso < distancia[w]:
                        # Reducir distancia y guardar de dónde venimos
                        distancia[w] = distancia[v] + peso
                        camino[w] = v
                        
        return distancia, camino

    def obtener_ruta_minima(self, origen, destino):
        # 1. Llamamos a Dijkstra para que nos calcule las tablas desde el origen
        distancias, caminos = self.dijkstra(origen)
        
        # 2. Verificamos si realmente se puede llegar al destino
        if distancias[destino] == float('inf'):
            return "No hay ruta disponible"
            
        # 3. Aquí va el fragmento que reconstruye el camino
        ruta = []
        actual = destino
        
        while actual is not None:
            ruta.append(actual)
            actual = caminos[actual]
            
        # 4. Invertimos y devolvemos la lista final
        return ruta[::-1]

    def warshall(self):
        # 1. Copiamos la matriz de adyacencia original
        P = self.__matriz.copy()
        n = self.__cantVertices
        
        # 2. Aplicamos los tres bucles anidados O(n^3)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # Actualizamos usando tu expresión lógica
                    P[i, j] = int(P[i, j] or (P[i, k] and P[k, j]))
                    
        return P

    def floyd(self):
        # Q = W (Copiamos la matriz de pesos/costos)
        Q = self.__matriz.copy()
        n = self.__cantVertices
        
        # Tres bucles anidados O(n^3)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # Q[i,j] = Mínimo (Q[i,j], Q[i,k] + Q[k,j])
                    Q[i, j] = min(Q[i, j], Q[i, k] + Q[k, j])
                    
        return Q

#Representacion encadenada
import heapq

class DigrafoEncadenado:
    def __init__(self, cant_vertices):
        self.__cantVertices = cant_vertices
        # Inicializamos una lista vacía para cada vértice
        self.__lista_ady = [[] for _ in range(cant_vertices)]

    def insertar_arista(self, origen, destino, peso=1):
        # Agregamos la tupla (destino, peso) a la lista del nodo origen
        self.__lista_ady[origen].append((destino, peso))

    def adyacentes(self, v):
        # Devolvemos solo los nodos destino para mantener compatibilidad con algoritmos previos
        return [destino for destino, peso in self.__lista_ady[v]]

    def orden_topologico(self):
        marca = [False] * self.__cantVertices
        resultado = []
        
        def topologico_visita(v):
            marca[v] = True
            for w in self.adyacentes(v):
                if not marca[w]:
                    topologico_visita(w)
            resultado.append(v)
            
        for v in range(self.__cantVertices):
            if not marca[v]:
                topologico_visita(v)
                
        return resultado[::-1]

    def dijkstra(self, origen):
        # Usamos una cola de prioridad (heap) para optimizar la búsqueda del menor costo
        distancia = [float('inf')] * self.__cantVertices
        camino = [None] * self.__cantVertices
        distancia[origen] = 0
        
        # Cola de prioridad: almacena tuplas (distancia_acumulada, nodo_actual)
        cola = [(0, origen)]
        
        while cola:
            dist_actual, u = heapq.heappop(cola)
            
            # Si encontramos una distancia mayor en la cola a la ya registrada, la ignoramos
            if dist_actual > distancia[u]:
                continue
                
            # Exploramos los vecinos directamente desde la lista de adyacencia
            for v, peso in self.__lista_ady[u]:
                nueva_dist = dist_actual + peso
                
                if nueva_dist < distancia[v]:
                    distancia[v] = nueva_dist
                    camino[v] = u
                    heapq.heappush(cola, (nueva_dist, v))
                    
        return distancia, camino