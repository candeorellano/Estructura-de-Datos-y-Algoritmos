class ListaOrdenadaSecuencial:
    __capacidad:int
    __elementos:list
    __cantidad:int

    def __init__(self, cap=100):
        self.__capacidad = cap
        self.__elementos = [None] * self.__capacidad
        self.__cantidad = 0

    #Funciones que cambian en esta implementación secuencial ordenada:
    def insertar(self, x):
        if self.__cantidad >= self.__capacidad:
            raise OverflowError("La lista esta llena")
        else:
            p = 0
            #buscamos la posicion para mantener el orden (menor a mayor)
            while p < self.__cantidad and self.__elementos[p] < x:
                p += 1

            for i in range(self.__cantidad, p, -1): #desplazamos hacia la derecha de esa posicion p
                self.__elementos[i] = self.__elementos[i-1]

            #insertamos el elemento en el hueco de la posicion p
            self.__elementos[p] = x
            self.__cantidad += 1 #incrementamos cantidad

    def buscar(self, x):
        i = 0

        while i < self.__cantidad and self.__elementos[i] < x:
            i += 1

        if i < self.__cantidad and self.__elementos[i] == x:
            return i+1
        else:
            raise ValueError("Error: Elemento no encontrado")

    #Funciones que se mantienen iguales
    def vacia(self):
        return self.__cantidad == 0

    def suprimir(self, p):
        if p < 1 or p > self.__cantidad:
            raise IndexError("Error: Posición inválida para suprimir")

        x = self.__elementos[p-1]

        for i in range(p-1, self.__cantidad - 1):
            self.__elementos[i] = self.__elementos[i+1] #le asigna a la posicion i lo que hay en la posicion i+1

        self.__elementos[self.__cantidad - 1] = None # pone como None a esa posicion
        self.__cantidad -= 1 #decrementa la cantidad
        return x
    
    def recuperar(self, p):
        if p < 1 or p > self.__cantidad:
            raise IndexError("Error: La posición es inválida para recuperar")

        x = self.__elementos[p-1]
        return x

    def primer_elemento(self):
        elem = None
        if not self.vacia():
            elem = self.__elementos[0]
            return elem
        else:
            raise IndexError("La lista está vacía")

    def ultimo_elemento(self):
        if not self.vacia():
            return self.__elementos[self.__cantidad - 1]
        else:
            raise IndexError("La lista está vacía")

    def siguiente(self, p):
        if 1 <= p < self.__cantidad:
            return p + 1
        else:
            raise IndexError("Error: No hay posicion siguiente")

    def anterior(self, p):
        if 1 < p <= self.__cantidad:
            return p - 1
        else:
            raise IndexError("Error: No hay posicion anterior")

    def recorrer(self,  operacion):
        for i in range(self.__cantidad):
            operacion(self.__elementos[i])