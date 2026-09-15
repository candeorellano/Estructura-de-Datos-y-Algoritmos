class ListaCursorSecuencial:
    __capacidad:int
    __cantidad:int
    __elementos:list
    __cursor:int

    def __init__(self, cap):
        self.__capacidad = cap
        self.__cantidad = 0
        self.__elementos = [None] * self.__capacidad
        self.__cursor = 0

    def vacia(self):
        return self.__cantidad == 0

    #Funciones de manejo del cursor
    def mover_cursor(self, p):
        if 1 <= p <= self.__cantidad:
            self.__cursor = p
        else:
            raise IndexError("Error: Posicion invalida para el cursor")

    def avanzar_cursor(self):
        if self.__cursor < self.__cantidad:
            self.__cursor += 1
        else:
            raise IndexError("Error: El cursor no puede seguir avanzando ya que esta en la ultima posicion")

    def reiniciar_cursor(self):
        if not self.vacia():
            self.__cursor = 1 #si no esta vacia, el cursor se pone en el primer elemento
        else:
            self.__cursor = 0 #si esta vacia, el cursor se pone al principio (cero)

    #Funciones tradicionales adaptadas
    def insertar(self, x):
        if self.__cantidad >= self.__capacidad:
            raise OverflowError("Error: la lista ya esta llena")

        # Si la lista estaba vacia, el cursor se inicializa en 1
        if self.vacia():
            self.__cursor = 1

        pos = self.__cursor #le asignamos a pos el numero del cursor

        for i in range(self.__cantidad, pos - 1, -1): # recorre desde la cantidad de elementos hasta el numero de posicion - 1, va hacia atrás
            self.__elementos[i] = self.__elementos[i - 1] #la posicion i de la lista toma el valor de la posicion i-1 de la lista (el que esta antes)

        self.__elementos[pos - 1] = x #la pos-1 de la lista toma el valor de x (hay un hueco)
        self.__cantidad += 1 #la cantidad se incrementa en uno

    def suprimir(self):
        if self.vacia() or self.__cursor == 0:
            raise IndexError("Error: No hay elementos para suprimir")

        pos = self.__cursor #la posicion es el numero del cursor
        x = self.__elementos[pos-1] #x toma el valor de lo que esta en la posicion-1 en la lista

        for i in range(pos - 1, self.__cantidad - 1): #arranca en posicion-1 y termina en cantidad-1
            self.__elementos[i] = self.__elementos[i+1]

        self.__elementos[self.__cantidad - 1] = None #pone la ultima posicion de la lista como None,ya que se elimina el elemento
        self.__cantidad -= 1

        #si eliminamos el ultimo elemento de la lista, el cursor debe retroceder
        if self.__cursor > self.__cantidad:
            self.__cursor = self.__cantidad

        return x #devuelve el valor que se suprimio

    def recuperar(self):
        if self.vacia() or self.__cursor == 0:
            raise IndexError("Error: No hay elementos para recuperar")
        return self.__elementos[self.__cursor - 1] #devuelve el elemento donde esta posicionado el cursor

    def buscar(self, x):
        if self.vacia():
            raise IndexError("Error: La lista esta vacia")
        
        i = 0
        encontrado = False

        while i < self.__cantidad and not encontrado:
            if self.__elementos[i] == x:
                encontrado = True
                self.__cursor = i + 1 #actualizamos el cursor en la posicion que esta el elemento
            else:
                i += 1

        if encontrado:
            return self.__cursor
        else:
            raise ValueError("Error: Elemento no encontrado")
