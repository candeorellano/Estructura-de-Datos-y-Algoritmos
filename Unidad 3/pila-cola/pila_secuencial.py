class Pila:
    __items: list[int]
    __tope: int
    __cant: int

    def __init__(self, xcant=0):
        self.__cant = xcant
        self.__tope = -1
        self.__items = [0] * self.__cant

    def vacia(self):
        return self.__tope == -1

    def insertar(self, x):
        if (self.__tope < self.__cant - 1):
            self.__tope += 1
            self.__items[self.__tope] = x
            return x
        else:
            return 0

    def suprimir(self):
        if self.vacia():
            print("Pila vacía")
            return 0
        else:
            x=self.__items[self.__tope]
            self.__tope -= 1
            return x

    def mostrar(self):
        if not self.vacia():
            for i in range(self.__tope, -1, -1):
                print(f"{self.__items[i]}")

if __name__ == "__main__":
    pila_sec = Pila(3)  # Instanciamos la pila con 3 elementos

    print("Insertando 10: ", pila_sec.insertar(10))
    print("Insertando 20: ", pila_sec.insertar(20))
    print("Insertando 30: ", pila_sec.insertar(30))

    print("Intentando insertar 40: ", pila_sec.insertar(40))

    print("Contenido de la pila (del tope a base)")
    pila_sec.mostrar()

    print("Suprimiendo el tope:", pila_sec.suprimir())
    
    #Suprimimos todo de la pila
    pila_sec.suprimir() # Saca el 20
    pila_sec.suprimir() # Saca el 10
    print("Intentando suprimir en pila vacía:")
    pila_sec.suprimir() # Debería imprimir "Pila vacía" y devolver 0