from __future__ import annotations

class Nodo:
    __dato: int #puede ser de cualquier otro tipo
    __siguiente: object

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def getDato(self):
        return self.__dato

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

class Lista:
    __cab: Nodo
    __cantidad: int

    def __init__(self):
        self.__cab = None
        self.__cantidad = 0

    def vacia(self):
        return self.__cantidad == 0

    def insertar(self, x, p):
        if p<1 or p>self.__cantidad + 1:
            raise IndexError("Error: Posición inválida para insertar")
        else:
            nuevo_nodo = Nodo(x)

            if p == 1: #insercion al principio de la lista
                nuevo_nodo.setSiguiente(self.__cab)
                self.__cab = nuevo_nodo
            else: #innsercion en el medio o al final
                aux = self.__cab

                for i in range(1, p-1):
                    aux = aux.getSiguiente()

                nuevo_nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nuevo_nodo)

            self.__cantidad += 1

    def suprimir(self, p):
        if p<1 or p>self.__cantidad:
            raise IndexError("Error: Posicion invalida para suprimir")
        else:
            if p == 1:
                dato_elim = self.__cab.getDato()
                self.__cab = self.__cab.getSiguiente()
            else:
                aux = self.__cab

                for i in range(1, p-1):
                    aux = aux.getSiguiente()

                dato_elim = aux.getSiguiente().getDato()
                aux.setSiguiente(aux.getSiguiente().getSiguiente())

            self.__cantidad -= 1
            return dato_elim

    def recuperar(self, p):
        if p < 1 or p > self.__cantidad:
            raise IndexError("Error: Posicion invalida para recuperar")
        else:
            aux = self.__cab
            for i in range(1, p):
                aux = aux.getSiguiente()

            return aux.getDato()

    def buscar(self, x):
        aux = self.__cab
        pos = 1
        encontrado = False

        while aux is not None and not encontrado:
            if aux.getDato() == x:
                encontrado = True
            else:
                aux = aux.getSiguiente()
                pos += 1

        if encontrado == True:
            return pos
        else: 
            raise ValueError("El elemento no fue encontrado")

    def primer_elemento(self):
        if not self.vacia():
            return self.__cab.getDato()
        else:
            raise IndexError("La lista está vacía")

    def ultimo_elemento(self):
        if self.vacia():
            raise IndexError("La lista está vacía")
        else:
            aux = self.__cab

            while aux.getSiguiente() is not None:
                aux = aux.getSiguiente()

            return aux.getDato()

    def siguiente(self,p):
        if self.vacia():
            raise IndexError("La lista esta vacía")

        if 1 <= p < self.__cantidad:
            return p+1
        else:
            raise IndexError("No hay posicion siguiente")

    def anterior(self, p):
        if self.vacia():
            raise IndexError("La lista esta vacia")

        if 1 < p <= self.__cantidad:
            return p-1
        else:
            raise IndexError("No hay posicion anterior")

    def recorrer(self, operacion):
        if self.vacia():
            raise IndexError("La lista esta vacia")

        aux = self.__cab

        while aux is not None:
            operacion(aux.getDato())
            aux = aux.getSiguiente()

    