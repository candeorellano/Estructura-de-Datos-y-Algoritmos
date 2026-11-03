class Nodo:
    __dato:int
    __izquierda:'Nodo'
    __derecha: 'Nodo'

    def __init__(self, dato):
        self.__dato = dato
        self.__izquierda = None
        self.__derecha = None

    def get_dato(self): 
        return self.__dato
    def set_dato(self, dato):
        self.__dato = dato
    
    def get_izquierda(self): 
        return self.__izquierda
    def set_izquierda(self, nodo): 
        self.__izquierda = nodo
    
    def get_derecha(self): 
        return self.__derecha
    def set_derecha(self, nodo): 
        self.__derecha = nodo

class ArbolBinarioBusqueda:
    __raiz: Nodo

    def __init__(self):
        self.__raiz = None

    def vacio(self):
        return self.__raiz is None

    def insertar(self, dato):
        # Disparamos la recursión empezando por la raíz
        self.__raiz = self.insertar_recursivo(self.__raiz, dato)

    def insertar_recursivo(self, nodo, dato):
        # 1. Si (sub)árbol vacío -> entonces Éxito - X nueva hoja
        if nodo is None:
            nodo = Nodo(dato)
        else:
            # 2. Si Clave X = Clave R -> Elemento ya existente
            if dato == nodo.get_dato():
                raise ValueError(f"Error: Elemento {dato} ya existente")

            # 3. Si Clave X < Clave R -> Insertar en subárbol izquierdo
            elif dato < nodo.get_dato():
                nodo.set_izquierda(self.insertar_recursivo(nodo.get_izquierda(), dato))

            # 4. sino -> Insertar en subárbol derecho
            else:
                nodo.set_derecha(self.insertar_recursivo(nodo.get_derecha(), dato))

        # Retornamos el nodo actual para reconstruir los enlaces en la recursión
        return nodo

    def suprimir(self, dato):
        self.__raiz = self.suprimir_recursivo(self.__raiz, dato)

    def suprimir_recursivo(self, nodo, dato):
        # Si (sub)árbol vacío -> Error -elemento inexistente
        if nodo is None:
            raise ValueError(f"Error: Elemento {dato} inexistente")
        else:
            # Si Clave X = Clave R (Lo encontramos)
            if dato == nodo.get_dato():
                # Si Grado(R) = 0 o Grado(R) = 1 (Hoja o un solo hijo)
                if nodo.get_izquierda() is None:
                    nodo = nodo.get_derecha() # Padre(R) <- Hijo(R) (Sube el derecho o None)
                elif nodo.get_derecha is None:
                    nodo = nodo.get_izquierda() # Padre(R) <- Hijo(R) (Sube el izquierdo)

                # Si Grado(R) = 2 (Dos hijos)
                else:
                    # 1. R <- Máximo ((sub)árbol-izquierdo (R))
                    predecesor =  self.obtener_maximo(nodo.get_izquierda())
                    nodo.set_dato(predecesor.get_dato())

                    # 2. Eliminar (Máximo((sub)árbol-izquierdo(R)))
                    nodo.set_izquierda(self.suprimir_recursivo(nodo.get_izquierda, predecesor.get_dato()))

            # Si Clave X < clave R
            elif dato < nodo.get_dato():
                nodo.set_izquierda(self.suprimir_recursivo(nodo.get_izquierda, dato))

            # sino (Clave X > clave R)
            else:
                nodo.set_derecha(self.suprimir_recursivo(nodo.get_derecha(), dato))
                
        return nodo

    # Método auxiliar para encontrar el valor más grande de un subárbol
    def obtener_maximo(self, nodo):
        actual = nodo

        # El mayor valor siempre está lo más a la derecha posible
        while actual.get_derecha() is not None:
            actual = actual.get_derecha()
        return actual

    def buscar(self, dato):
        return self.buscar_recursivo(self.__raiz, dato)

    def buscar_recursivo(self, nodo, dato):
        valor = None
        #Si (sub)arbol vacio -> Error
        if nodo is None:
            raise ValueError(f"Error: Elemento {dato} inexistente")
        else:
            if dato == nodo.get_dato():
                valor = nodo
            elif dato < nodo.get_dato():
                valor = self.buscar_recursivo(nodo.get_izquierda(), dato)
            else:
                valor = self.buscar_recursivo(nodo.get_derecha(), dato)

        return valor

    #PREORDEN
    def preorden(self):
        self.preorden_recursivo(self.__raiz)
        print() #salto de linea

    def preorden_recursivo(self, nodo):
        #Si Arbol No Vacio
        if nodo is not None:
            #Procesar Nodo R
            print(nodo.get_dato())
            #Subarbol izq
            self.preorden_recursivo(nodo.get_izquierda())
            #Subarbol der
            self.preorden_recursivo(nodo.get_derecha())

    #INORDEN
    def inorden(self):
        self.inorden_recursivo(self.__raiz)
        print()

    def inorden_recursivo(self, nodo):
        if nodo is not None:
            #Subarbol izq
            self.inorden_recursivo(nodo.get_izquierda())
            #Procesar Nodo R
            print(nodo.get_dato())
            #Subarbol der
            self.inorden_recursivo(nodo.get_derecha())

    #POSTORDEN
    def postorden(self):
        self.postorden_recursivo(self.__raiz)

    def postorden_recursivo(self, nodo):
        if nodo is not None:
            #Subarbol izq
            self.postorden_recursivo(nodo.get_izquierda())
            #Subarbol der
            self.postorden_recursivo(nodo.get_derecha())
            #Procesar Nodo R
            print(nodo.get_dato())

    def getRaiz(self):
        return self.__raiz

    