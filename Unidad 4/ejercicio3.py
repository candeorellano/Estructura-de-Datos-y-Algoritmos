class NodoAVL:
    def __init__(self, dato):
        self.__dato = dato
        self.__izquierda = None
        self.__derecha = None
        self.__bal = 0  # Factor de balance: -1, 0 o 1

    # Getters y Setters
    def get_dato(self): return self.__dato
    def set_dato(self, dato): self.__dato = dato
    
    def get_izquierda(self): return self.__izquierda
    def set_izquierda(self, izq): self.__izquierda = izq
    
    def get_derecha(self): return self.__derecha
    def set_derecha(self, der): self.__derecha = der
    
    def get_bal(self): return self.__bal
    def set_bal(self, bal): self.__bal = bal


class ArbolAVL:
    def __init__(self):
        self.__raiz = None

    def insertar(self, dato):
        # La función recursiva nos devuelve la nueva raíz y un booleano (si creció o no)
        self.__raiz, crecio = self._insertar_recursivo(self.__raiz, dato)

    def _insertar_recursivo(self, nodo, dato):
        # 1. Si el árbol está vacío, creamos el nodo
        if nodo is None:
            return NodoAVL(dato), True  # True significa que el árbol creció en altura

        # 2. Si el dato ya existe
        if dato == nodo.get_dato():
            raise ValueError(f"Error: Elemento {dato} ya existente")

        crecio = False

        # 3. Insertar a la izquierda
        if dato < nodo.get_dato():
            nodo_izq, crecio = self._insertar_recursivo(nodo.get_izquierda(), dato)
            nodo.set_izquierda(nodo_izq)

            # Si el subárbol izquierdo creció, revisamos el balance de este nodo
            if crecio:
                if nodo.get_bal() == 1:       # Estaba inclinado a la derecha, ahora se equilibra
                    nodo.set_bal(0)
                    crecio = False
                elif nodo.get_bal() == 0:     # Estaba equilibrado, ahora se inclina a la izquierda
                    nodo.set_bal(-1)
                elif nodo.get_bal() == -1:    # Ya estaba inclinado a la izquierda... ¡DESBALANCE!
                    # Aquí aplicamos las rotaciones
                    nodo1 = nodo.get_izquierda()
                    if nodo1.get_bal() == -1:
                        # Signos iguales: ROTACIÓN SIMPLE (Ej: el caso 7 -> 5 -> 2)
                        nodo = self._rotacion_simple_derecha(nodo, nodo1)
                    else:
                        # Signos distintos: ROTACIÓN DOBLE
                        nodo = self._rotacion_doble_izquierda_derecha(nodo, nodo1)
                    crecio = False # Después de rotar, el árbol vuelve a su altura original

        # 4. Insertar a la derecha
        else:
            nodo_der, crecio = self._insertar_recursivo(nodo.get_derecha(), dato)
            nodo.set_derecha(nodo_der)

            # Si el subárbol derecho creció
            if crecio:
                if nodo.get_bal() == -1:      # Estaba inclinado a la izquierda, ahora se equilibra
                    nodo.set_bal(0)
                    crecio = False
                elif nodo.get_bal() == 0:     # Estaba equilibrado, ahora se inclina a la derecha
                    nodo.set_bal(1)
                elif nodo.get_bal() == 1:     # Ya estaba inclinado a la derecha... ¡DESBALANCE!
                    nodo1 = nodo.get_derecha()
                    if nodo1.get_bal() == 1:
                        # Signos iguales: ROTACIÓN SIMPLE
                        nodo = self._rotacion_simple_izquierda(nodo, nodo1)
                    else:
                        # Signos distintos: ROTACIÓN DOBLE
                        nodo = self._rotacion_doble_derecha_izquierda(nodo, nodo1)
                    crecio = False

        return nodo, crecio

    # ==========================================
    #             ROTACIONES
    # ==========================================

    def _rotacion_simple_derecha(self, nodo, nodo1):
        # nodo es el 7, nodo1 es el 5
        nodo.set_izquierda(nodo1.get_derecha())
        nodo1.set_derecha(nodo)
        
        # Arreglamos los balances
        nodo.set_bal(0)
        nodo1.set_bal(0)
        
        return nodo1 # El 5 sube y se convierte en la nueva raíz de este subárbol

    def _rotacion_simple_izquierda(self, nodo, nodo1):
        nodo.set_derecha(nodo1.get_izquierda())
        nodo1.set_izquierda(nodo)
        
        nodo.set_bal(0)
        nodo1.set_bal(0)
        
        return nodo1

    def _rotacion_doble_izquierda_derecha(self, nodo, nodo1):
        nodo2 = nodo1.get_derecha()
        nodo1.set_derecha(nodo2.get_izquierda())
        nodo2.set_izquierda(nodo1)
        nodo.set_izquierda(nodo2.get_derecha())
        nodo2.set_derecha(nodo)

        # Ajuste de balances dependiendo de dónde se insertó el nuevo nodo
        if nodo2.get_bal() == -1:
            nodo.set_bal(1)
        else:
            nodo.set_bal(0)
            
        if nodo2.get_bal() == 1:
            nodo1.set_bal(-1)
        else:
            nodo1.set_bal(0)
            
        nodo2.set_bal(0)
        return nodo2

    def _rotacion_doble_derecha_izquierda(self, nodo, nodo1):
        nodo2 = nodo1.get_izquierda()
        nodo1.set_izquierda(nodo2.get_derecha())
        nodo2.set_derecha(nodo1)
        nodo.set_derecha(nodo2.get_izquierda())
        nodo2.set_izquierda(nodo)

        if nodo2.get_bal() == 1:
            nodo.set_bal(-1)
        else:
            nodo.set_bal(0)
            
        if nodo2.get_bal() == -1:
            nodo1.set_bal(1)
        else:
            nodo1.set_bal(0)
            
        nodo2.set_bal(0)
        return nodo2