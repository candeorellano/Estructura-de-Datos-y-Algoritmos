from lista_encadenada_A import Nodo

class ListaEncadenadaOrdenada:
    __cab: Nodo
    __cantidad: int

    def __init__(self):
        self.__cab = None
        self.__cantidad = 0

    def vacia(self):
        return self.__cantidad == 0

    #Funciones que cambian en esta implementacion encadenada ordenada
    def insertar(self, x):
        nuevo_nodo = Nodo(x)

        #insercion al principio
        if self.vacia() or x < self.__cab.getDato():
            nuevo_nodo.setSiguiente(self.__cab)
            self.__cab = nuevo_nodo
        else: #insercion en el medio o al final
            aux = self.__cab

            # avanzamos mientras el nodo siguiente no sea None (exista) y el dato de ese nodo siguiente sea menor que x
            while aux.getSiguiente() is not None and aux.getSiguiente.getDato() < x:
                aux = aux.getSiguiente()

            #encontramos la posicion. enlazamos el nuevo nodo
            nuevo_nodo.setSiguiente(aux.getSiguiente())
            aux.setSiguiente(nuevo_nodo)
    
    def buscar(self, x):
        aux = self.__cab
        encontrado = False
        pos = 1

        while aux is not None and not encontrado and aux.getDato() <= x:
            if aux.getDato() == x:
                encontrado = True
            else:
                aux = aux.getSiguiente()
                pos += 1

        if encontrado:
            return pos
        else:
            raise ValueError("Error: Elemento no encontrado")


    #Funciones que se mantienen iguales

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
    