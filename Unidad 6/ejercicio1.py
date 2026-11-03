import numpy as np

#Representación Secuencial
class GrafoSecuencial:
    __cantidadVertices:int
    __matriz:np.ndarray

    def __init__(self, xvertices):
        self.__cantidadVertices = xvertices
        self.__matriz = np.zeros((self.__cantidadVertices, self.__cantidadVertices), dtype=int)

    def getCantVertices(self):
        return self.__cantidadVertices

    def getMatriz(self):
        return self.__matriz

    def adyacentes(self, u):
        lista_vecinos = []

        for v in range(self.__cantidadVertices):
            if self.__matriz[u,v] == 1:
                lista_vecinos.append(v)

        return lista_vecinos

    def camino(self, u, v):
        pass
    
#Representación Encadenada
class GrafoEncadenado:
    __cantVertices:int
    __listasAdyacencia:list

    def __init__(self, xvertices):
        self.__cantVertices = xvertices
        self.__listasAdyacencia = []

        for vertice in range(self.__cantVertices):
            self.__listasAdyacencia.append([])

    def getCantVertices(self):
        return self.__cantVertices

    def adyacentes(self, u):
        return self.__listasAdyacencia[u]

    def rep(self):
        # Arreglos de descubrimiento (d) y finalización (f)
        d = [0] * self.__cantVertices
        f = [0] * self.__cantVertices
        tiempo = [0] # Reloj global
        
        # Evaluamos cada vértice del grafo
        for s in range(self.__cantVertices):
            if d[s] == 0:
                self._rep_visita(s, d, f, tiempo)

    def repVisita(self, s, d, f, tiempo):
        tiempo[0] += 1
        d[s] = tiempo[0] # Registramos el momento de descubrimiento

        # Iteramos sobre los vecinos usando el método que creamos antes
        for u in self.adyacentes(s):
            if d[u] == 0:
                self.repVisita(u, d, f, tiempo)

        tiempo[0] += 1
        f[s] = tiempo[0] # Registramos el momento de finalización (todas sus ramas exploradas)

    def rea(self, s):
        d = [float('inf')] * self.__cantVertices
        cola = []

        d[s] = 0
        cola.append(s)

        while len(cola) > 0:
            v = cola.pop(0)

            for u in self.adyacentes(v):
                if d[u] == float('inf'):
                    d[u] = d[v] + 1
                    cola.append(u)

        return d

    def conexo(self):
        # Verificamos si el grafo está vacío para evitar errores
        if self.__cantVertices == 0:
            return True

        # Lanzamos el REA desde el vértice 0
        distancias = self.rea(0)

        # Revisamos si quedó algún nodo inalcanzable
        for d in distancias:
            if d == float('inf'):
                return False # Encontramos un nodo desconectado

        return True # Todos los nodos fueron alcanzados

    def aciclico(self):
        d = [0] * self.__cantVertices

        for s in range(self.__cantVertices):
            if d[s] == 0:
                if self.detectarCiclo(s, d, -1):
                    return False

        return True

    def detectarCiclo(self, s, d, padre):
        d[s] = 1

        