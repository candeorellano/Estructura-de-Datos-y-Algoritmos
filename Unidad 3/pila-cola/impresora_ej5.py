import random
from cola_encadenada import Cola

class Trabajo:
    __id: int
    __tiempo_llegada: int
    __tiempo_original: int
    __tiempo_restante:int

    def __init__(self, id_trabajo, tiempo_llegada, tiempo_impresion):
        self.__id = id_trabajo
        self.__tiempo_llegada = tiempo_llegada
        self.__tiempo_original = tiempo_impresion
        self.__tiempo_restante = tiempo_impresion

    def getOriginal(self):
        return self.__tiempo_original

    def getRestante(self):
        return self.__tiempo_restante
    
    def getId(self):
        return self.__id

    def getLlegada(self):
        return self.__tiempo_llegada

    def setRestante(self, minutos):
        self.__tiempo_restante -= minutos

    
def simular_impresora():
    cola_impresion = Cola()

    reloj = 0
    acumu_espera = 0
    impresos = 0
    prox_llegada = 0
    id_trabajo = 1

    while reloj < 60:
        while prox_llegada <= reloj and prox_llegada < 60:
            tiempo_req = random.randint(2,12)
            nuevo_trab = Trabajo(id_trabajo, prox_llegada, tiempo_req)
            cola_impresion.insertar(nuevo_trab)
            print(f"[{prox_llegada}] Llega trabajo {nuevo_trab.getId()} (Demora total: {tiempo_req} minutos)")
            prox_llegada += 5
            id_trabajo += 1

        if cola_impresion.vacia():
            reloj = prox_llegada
            continue

        trabajo = cola_impresion.suprimir()

        if trabajo.getRestante() <= 5:
            reloj += trabajo.getRestante()

            tiempo_espera = reloj - trabajo.getLlegada() - trabajo.getOriginal()
            acumu_espera += tiempo_espera
            impresos += 1

            print(f"[{reloj}'] Terminó Trabajo {trabajo.getId()}. Esperó en cola: {tiempo_espera} min.")
        else:
            reloj += 5

            trabajo.setRestante(5)

            while prox_llegada <= reloj and prox_llegada < 60:
                tiempo_req = random.randint(2, 12)
                nuevo_trab = Trabajo(id_trabajo, prox_llegada, tiempo_req)
                cola_impresion.insertar(nuevo_trab)
                print(f"[{prox_llegada}'] Llega Trabajo {nuevo_trab.getId()} (Demora Total: {tiempo_req} min)")
                prox_llegada += 5
                id_trabajo += 1

            cola_impresion.insertar(trabajo)
            print(f"[{reloj}'] Trabajo {trabajo.getId()} reencolado (Le restan {trabajo.getRestante()} min).")

    # Fin de Simulación: Contar elementos en la cola
    trabajos_sin_atender = 0
    while not cola_impresion.vacia():
        cola_impresion.suprimir()
        trabajos_sin_atender += 1

    promedio = acumu_espera / impresos if impresos > 0 else 0

    print("\n" + "="*45)
    print("RESULTADOS FINALES AL MINUTO 60:")
    print(f"a) Trabajos que quedaron sin atender (en cola): {trabajos_sin_atender}")
    print(f"b) Promedio de espera (trabajos impresos): {promedio:.2f} minutos")
    print("="*45)

if __name__ == "__main__":
    simular_impresora()
