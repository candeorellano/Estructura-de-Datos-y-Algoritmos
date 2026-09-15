class Cola:
    __items: list[int]
    __max: int
    __pr: int
    __ul: int
    __cant: int

    def __init__(self, xmax=0):
        self.__max = xmax
        self.__pr = 0
        self.__ul = 0
        self.__cant = 0
        self.__items = [0] * self.__max

    def vacia(self):
        return self.__cant == 0

    def insertar(self, x):
        if (self.__cant < self.__max):
            self.__items[self.__ul] = x
            self.__ul = (self.__ul + 1) % self.__max
            self.__cant += 1
            return x
        else:
            return 0

    def suprimir(self):
        if self.vacia():
            print(f"Cola vacia")
            return 0
        else:
            x = self.__items[self.__pr]
            self.__pr=(self.__pr + 1) % self.__max
            self.__cant -= 1
            return x
        
    def recorrer(self):
        if not self.vacia():
            i = self.__pr
            j=0
            # Iteramos exactamente la cantidad de elementos actuales
            for j in range(self.__cant):
                print(self.__items[i])
                i = (i + 1) % self.__max

    def longitud(self): # para ejercicio 6
        return self.__cant
    
if __name__ == "__main__":
    print("INICIANDO PRUEBAS: COLA SECUENCIAL (CIRCULAR)")
    
    # 1. Creamos una cola con capacidad MÁXIMA de 3 elementos
    mi_cola_sec = Cola(3)
    
    # 2. Llenamos la cola
    print("Insertando 10:", mi_cola_sec.insertar(10))
    print("Insertando 20:", mi_cola_sec.insertar(20))
    print("Insertando 30:", mi_cola_sec.insertar(30))
    
    # 3. Prueba de límite: Intentamos insertar cuando está llena
    print("Intentando insertar 40 (debería fallar):", mi_cola_sec.insertar(40))
    
    print("\nEstado de la cola llena:")
    mi_cola_sec.recorrer()
    
    # 4. Atendemos a una persona (liberamos 1 espacio)
    print("\nSalió de la cola el:", mi_cola_sec.suprimir())
    
    # 5. PRUEBA CIRCULAR: Insertamos otro elemento. 
    # Como el espacio libre está al principio del arreglo, el puntero debe dar la vuelta.
    print("Insertando 50 (aprovechando el espacio circular):", mi_cola_sec.insertar(50))
    
    print("\nEstado final de la cola (debería mostrar 20, 30, 50):")
    mi_cola_sec.recorrer()