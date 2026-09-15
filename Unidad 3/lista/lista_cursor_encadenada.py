from lista_encadenada_A import Nodo

class ListaEncadenadaCursor:
    __cab = Nodo
    __cant = int
    __cursor = Nodo

    def __init__(self):
        self.__cab = None
        self.__cursor = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0

    #Funciones de manejo del cursor

    def mover_cursor(self, p):
        if 1 <= p <= self.__cant:
            aux = self.__cab

            for _ in range(1, p): #va de 1 hasta la posicion p
                aux = aux.getSiguiente()

            self.__cursor = aux
        else:
            raise IndexError("Error: Posicion invalida para el cursor")

    def avanzar_cursor(self):
        if self.__cursor is not None and self.__cursor.getSiguiente() is not None:
            self.__cursor = self.__cursor.getSiguiente()
        else:
            raise IndexError("Error: el cursor no puede seguir avanzando")

    def reiniciar_cursor(self):
        self.__cursor = self.__cab #si esta vacia, la cabeza es None

    #Funciones tradicionales adaptadas

    def insertar(self, x):
        nuevo_nodo = Nodo(x)

        if self.vacia():
            self.__cab = nuevo_nodo
            self.__cursor = nuevo_nodo
        elif self.__cursor == self.__cab: #ya hay un elemento en la lista
            nuevo_nodo.setSiguiente(self.__cab)
            self.__cab = nuevo_nodo
            self.__cursor = nuevo_nodo
        else: #insercion en el medio o en el final
            aux = self.__cab

            while aux.getSiguiente() is not self.__cursor:
                aux = aux.getSiguiente()

            nuevo_nodo.setSiguiente(self.__cursor)
            aux.setSiguiente(nuevo_nodo)
            self.__cursor = nuevo_nodo

        self.__cant += 1

    
                