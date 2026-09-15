class Lista:
    __capacidad:int
    __elementos: list
    __cantidad:int

    def __init__(self, cap=100):
        self.__capacidad = cap
        self.__elementos = [None] * self.__capacidad
        self.__cantidad = 0

    def vacia(self):
        return self.__cantidad == 0
    
    def insertar(self, x ,p):
        if p < 1 or p > self.__cantidad + 1:
            raise IndexError("Error: Posición inválida para insertar")
        if self.__cantidad >= self.__capacidad:
            raise OverflowError("Error: La lista está llena")

        for i in range(self.__cantidad, p-1, -1):
            self.__elementos[i] = self.__elementos[i-1] #le asigna a la posicion i lo que hay en la posicion i-1

        self.__elementos[p-1] = x #inserta el elemento en la posicion p-1 (ya que las posiciones empiezan en 0)
        self.__cantidad += 1 #incrementa la cantidad

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

    def buscar(self, x):
        i = 0
        encontrado = False
        while i < self.__cantidad and encontrado == False:
            if x == self.__elementos[i]:
                encontrado = True
                pos = i+1
            else:
                i += 1

        if encontrado == True:
            return pos
        else:
            raise ValueError("Error: Elemento no encontrado")

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