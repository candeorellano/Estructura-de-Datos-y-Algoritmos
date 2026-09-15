from __future__ import annotations

class Celda:
    __item: int
    __sig: Celda | None

    def __init__(self):
        self.__item = 0
        self.__sig = None

    def obteneritem(self):
        return self.__item

    def cargaritem(self, xitem):
        self.__item = xitem

    def cargarsig(self, xtope: Celda | None):
        self.__sig = xtope

    def obtenersig(self) -> Celda | None:
        return self.__sig

class Cola:
    __cant: int
    __pr: Celda | None
    __ul: Celda | None

    def __init__(self, xpr: Celda | None = None, xul: Celda | None = None, xcant = 0):
        self.__pr = xpr
        self.__ul = xul
        self.__cant = xcant

    def vacia(self):
        return self.__cant == 0

    def insertar(self, x):
        ps1 = Celda()
        ps1.cargaritem(x)
        ps1.cargarsig(None)

        if self.__ul is None:
            self.__pr = ps1
        else:
            self.__ul.cargarsig(ps1)
        self.__ul = ps1
        self.__cant += 1
        return self.__ul.obteneritem()

    def suprimir(self):
        if self.__pr is None: #if self.vacia():
            print("Cola vacia")
            return 0
        else:
            aux = self.__pr
            x = self.__pr.obteneritem()
            self.__pr = self.__pr.obtenersig()
            self.__cant -= 1
            if self.__pr is None:
                self.__ul = None
            return x

    def recuperapr(self) -> Celda | None:
        return self.__pr

    def recorrer(self, aux: Celda | None):
        if aux is not None:
            print(aux.obteneritem())
            self.recorrer(aux.obtenersig())

if __name__ == "__main__":
    print("INICIANDO PRUEBAS: COLA ENCADENADA")
    
    mi_cola = Cola()
    
    # 1. Insertamos elementos (hacen la fila)
    print("Entra a la cola el:", mi_cola.insertar(10))
    print("Entra a la cola el:", mi_cola.insertar(20))
    print("Entra a la cola el:", mi_cola.insertar(30))
    
    # 2. Recorremos la cola usando la función recursiva
    print("\nEstado actual de la cola (del primero al último):")
    # Le pasamos el puntero del primero para que empiece a recorrer
    mi_cola.recorrer(mi_cola.recuperapr()) 
    
    # 3. Suprimimos elementos (se atienden por orden de llegada)
    print("\nAtendiendo la cola:")
    print("Salió el:", mi_cola.suprimir()) # ¡Debería salir el 10!
    print("Salió el:", mi_cola.suprimir()) # ¡Debería salir el 20!
    
    # 4. Verificamos cómo quedó
    print("\nEstado de la cola después de atender a dos:")
    mi_cola.recorrer(mi_cola.recuperapr())