from __future__ import annotations

class Celda:
    __item: int
    __sig: Celda | None

    def __init__(self):
        self.__item = 0
        self.__sig = None

    def obteneritem(self):
        return self.__item

    def cargaritem(self, xitem: int):
        self.__item = xitem

    def cargarsig(self, xtope: Celda | None):
        self.__sig = xtope

    def obtenersig(self) -> Celda | None:
        return self.__sig

class Pila:
    __cant: int
    __tope: Celda | None

    def __init__(self, xtope: Celda | None = None, xcant: int = 0):
        self.__tope = xtope
        self.__cant = xcant

    def vacia(self) -> bool:
        return self.__cant == 0

    def insertar(self, x: int):
        ps1 = Celda()
        ps1.cargaritem(x)
        ps1.cargarsig(self.__tope)
        self.__tope = ps1
        self.__cant += 1

        return ps1.obteneritem()

    def suprimir(self):
        if self.__tope is None: #if self.vacia(). Se modifico para que no de error en las lineas de abajo
            print("Pila vacia")
            return 0
        else:
            # Al verificar que no es None arriba, el linter sabe que acá es una Celda
            aux=self.__tope
            x=self.__tope.obteneritem()
            self.__tope = self.__tope.obtenersig()
            self.__cant -= 1
            #El garbage collector destruye automaticamente la celda vieja en Python
            return x

    def mostrar(self):
        if self.vacia():
            print("Pila vacía")
        else:
            actual = self.__tope

            while actual is not None:
                print(f"  {actual.obteneritem()}")
                actual = actual.obtenersig()

if __name__ == "__main__":
    # 1. Instanciamos la pila (no requiere límite inicial)
    pila_enc = Pila()

    # 2. Insertamos elementos
    print("Insertando 100:", pila_enc.insertar(100))
    print("Insertando 200:", pila_enc.insertar(200))
    print("Insertando 300:", pila_enc.insertar(300))

    # 3. Suprimimos elementos y comprobamos el orden LIFO (Last In, First Out)
    print("Extrayendo elementos:")
    print("Salió el:", pila_enc.suprimir()) # Debería ser 300
    print("Salió el:", pila_enc.suprimir()) # Debería ser 200
    print("Salió el:", pila_enc.suprimir()) # Debería ser 100

    # 4. PRUEBA LÍMITE: Suprimir en pila dinámica vacía
    print("Intentando suprimir en pila vacía:")
    pila_enc.suprimir() # Debería imprimir "Pila vacia" y devolver 0