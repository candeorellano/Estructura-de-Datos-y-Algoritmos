from ejercicio1 import ArbolBinarioBusqueda

class ArbolEjercicio2(ArbolBinarioBusqueda):
    #Inciso 2.a)
    def mostrar_padre_hermano(self, dato):
        self.buscar_padre_hermano(self.getRaiz(),None, dato) #None es el padre

    def buscar_padre_hermano(self, nodo, padre, dato):
        if nodo is None:
            print(f"El nodo {dato} no esta en el arbol")
        else:
            if dato == nodo.get_dato():
                if padre is None:
                    print(f"El dato {dato} es la raiz. No tiene ni padre ni hermano")
                else:
                    print(f"Para {dato} -> Padre: {padre.get_dato()}")

                    if padre.get_izquierda() == nodo:
                        hermano = padre.get_derecha()
                    else:
                        hermano = padre.get_izquierda()

                    if hermano is None:
                        print("hermano: no existe (es hijo unico)")
                    else:
                        print(f"hermano: {hermano.get_dato()}")

            elif dato < nodo.get_dato():
                self.buscar_padre_hermano(nodo.get_izquierda(), nodo, dato)
            else:
                self.buscar_padre_hermano(nodo.get_derecha(), nodo, dato)

    #Inciso 2.b)
    def contar_nodos(self):
        return self.contar_recursivo(self.getRaiz())

    def contar_recursivo(self, nodo):
        valor = 0
        if nodo is None:
            valor = 0
        else:
            valor = 1 + self.contar_recursivo(nodo.get_derecha()) + self.contar_recursivo(nodo.get_izquierda())

        return valor

    #Inciso 2.c)
    def altura(self):
        return self._altura_recursiva(self.get_raiz())

    def _altura_recursiva(self, nodo):
        valor = 0
        if nodo is None:
            valor = -1
        else:
            altura_izq = self._altura_recursiva(nodo.get_izquierda())
            altura_der = self._altura_recursiva(nodo.get_derecha())
            
            # 1 + max(altura(n.izq), altura(n.der))
            valor = 1 + max(altura_izq, altura_der)
            
        return valor

    def mostrar_sucesores(self, dato):
        nodo_encontrado = self.buscar(dato)

        if nodo_encontrado is None:
            print(f"El nodo {dato} no existe en el arbol")
        else:
            print(f"Los sucesores de {dato} son: ")
        # Imprimimos los subárboles esquivando el nodo original
            self.inorden_recursivo(nodo_encontrado.get_izquierda())
            self.inorden_recursivo(nodo_encontrado.get_derecha())
            print() # Salto de línea final

    