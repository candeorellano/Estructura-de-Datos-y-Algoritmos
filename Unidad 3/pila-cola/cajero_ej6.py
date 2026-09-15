from __future__ import annotations
# Asumimos que la clase Cola y Cliente ya están definidas
from cola_secuencial import Cola
import random

class Cliente:
    __id: int
    __timestamp_llegada: int

    def __init__(self, xid, xllegada=0):
        self.__id = xid
        self.__timestamp_llegada = xllegada

    def getId(self):
        return self.__id

    def getLlegada(self):
        return self.__timestamp_llegada

class Cajero:
    __id: int
    __time_atencion: int
    __cola: Cola
    __idCliente: Cliente | None
    __tick_actual: int

    def __init__(self, xid, xtimeAt, xcola):
        self.__id = xid
        self.__time_atencion = xtimeAt
        self.__cola = xcola
        self.__idCliente = None
        self.__tick_actual = 0

    def getCola(self) -> Cola:
        return self.__cola

    def getTiempoAtencion(self):
        return self.__time_atencion
        
    def getIdCliente(self):
        return self.__idCliente
        
    def getTickActual(self):
        return self.__tick_actual

    # Setters
    def setIdCliente(self, cliente: Cliente | None):
        self.__idCliente = cliente

    def restarTick(self):
        if self.__tick_actual > 0:
            self.__tick_actual -= 1

    def reiniciarTick(self):
        self.__tick_actual = self.__time_atencion

def elegirCajero(listaCajeros: list[Cajero]) -> Cajero:
    """
    Aplica las reglas del enrutador heurístico:
    1. Si hay cajeros libres y sin cola, elige uno al azar.
    2. Si todos están ocupados, elige la cola más corta.
    3. Si hay empate en la cola más corta, elige al azar.
    """
    # Paso 1: Buscar cajeros totalmente libres (sin cliente actual y cola vacía)
    cajeros_libres = []

    for cajero in listaCajeros:
        if cajero.getIdCliente() is None and cajero.getCola().vacia():
            cajeros_libres.append(cajero)

    if len(cajeros_libres) > 0:
        return random.choice(cajeros_libres)

    minima_long = listaCajeros[0].getCola().longitud()
    for cajero in listaCajeros:
        long_actual = cajero.getCola().longitud()
        if long_actual < minima_long:
            minima_long = long_actual

    cajeros_min = []
    for cajero in listaCajeros:
        if cajero.getCola().longitud() == minima_long:
            cajeros_min.append(cajero)

    return random.choice(cajeros_min)

if __name__ == "__main__":
    print("--- INICIANDO SIMULACIÓN DEL BANCO (120 MINUTOS) ---")
    
    # 1. Inicializamos las 3 colas en el main
    cola1 = Cola(100)
    cola2 = Cola(100)
    cola3 = Cola(100)
    
    # 2. Inicializamos los 3 cajeros (ID, tiempo_atencion, cola)
    # Tiempos según enunciado: Cajero 1 (5 min), Cajero 2 (3 min), Cajero 3 (4 min)
    cajero1 = Cajero(1, 5, cola1)
    cajero2 = Cajero(2, 3, cola2)
    cajero3 = Cajero(3, 4, cola3)
    
    cajeros = [cajero1, cajero2, cajero3]
    
    # 3. Variables para las estadísticas del final
    reloj = 0
    tms = 120
    
    id_cliente = 1
    frec_llegada = 2
    espera_maxima = 0
    clientes_atendidos = 0
    tiempo_espera_acumulado = 0
    
    print("Banco abierto. Esperando clientes...")

    while reloj < tms:
        probab_llegada = 1 / frec_llegada
        if random.random() < probab_llegada:
            nuevo_cliente = Cliente(id_cliente, reloj)
            cajero_elegido = elegirCajero(cajeros)
            cajero_elegido.getCola().insertar(nuevo_cliente)
            id_cliente += 1

        for cajero in cajeros:
            if cajero.getIdCliente() is None:
                if not cajero.getCola().vacia():
                    cliente_actual = cajero.getCola().suprimir()
                    espera = reloj - cliente_actual.getLlegada()
                    tiempo_espera_acumulado += espera
                    clientes_atendidos += 1

                    if espera > espera_maxima:
                        espera_maxima = espera

                    cajero.setIdCliente(cliente_actual)
                    cajero.reiniciarTick()

        reloj += 1

        for cajero in cajeros:
            if cajero.getIdCliente() is not None:
                cajero.restarTick()

            if cajero.getTickActual() == 0:
                cajero.setIdCliente(None)

    # Fin Mientras

    # RESOLUCIÓN DE INCISOS
    no_atendidos = 0
    espera_acum_no_atend = 0

    for cajero in cajeros:
        while not cajero.getCola().vacia():
            cliente_esperando = cajero.getCola().suprimir()
            espera_acum_no_atend += (tms - cliente_esperando.getLlegada())
            no_atendidos +=1

    #calculos finales
    prom_atendidos = 0
    if clientes_atendidos > 0:
        prom_atendidos = tiempo_espera_acumulado / clientes_atendidos

    prom_no_atendidos = 0
    if no_atendidos > 0:
        prom_no_atendidos = espera_acum_no_atend / no_atendidos

    print("Reportes del banco al cierre (120 minutos):")
    print(f"a) tiempo maximo de espera de clientes en la cola: {espera_maxima} minutos")
    print(f"b) cantidad de clientes atendidos: {clientes_atendidos} clientes")
    print(f"c) cantidad de clientes que quedaron sin atender: {no_atendidos} clientes")
    print(f"d) promedio de espera de los clientes atendidos: {prom_atendidos:.2f} minutos")
    print(f"e) promedio de espera de los clientes que quedaron sin atender: {prom_no_atendidos:.2f} minutos")


