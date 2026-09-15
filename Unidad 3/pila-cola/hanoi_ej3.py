from pila_encadenada import Pila

def ver_tope(pila: Pila):
    if pila.vacia():
        return None
    valor = pila.suprimir()
    pila.insertar(valor)
    return valor

def jugar_hanoi():
    print("--- JUEGO DE LAS TORRES DE HANOI ---")
    n = int(input("Ingrese el número de discos con el que va a jugar: "))
    
    # Estado inicial:
    torres = {
        1: Pila(),
        2: Pila(),
        3: Pila()
    }
    
    # Apilamos los discos en la torre 1 (el mayor abajo, el menor arriba)
    for i in range(n, 0, -1):
        torres[1].insertar(i)

    jugadas_realizadas = 0
    jugadas_minimas = (2**n) - 1 # Fórmula matemática de resolución óptima -> 2^n-1

    # El juego termina cuando la 1 y la 2 están vacías
    while (torres[1].vacia() and torres[2].vacia()) is False:
        print("Estado actual de las torres (de tope a base):")
        print("Torre 1:"); torres[1].mostrar()
        print("Torre 2:"); torres[2].mostrar()
        print("Torre 3:"); torres[3].mostrar()
        
        try:
            origen = int(input("\nIngrese la torre origen (1, 2 o 3): "))
            destino = int(input("Ingrese la torre destino (1, 2 o 3): "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        # BLOQUE DE VALIDACIONES        
        if origen not in [1, 2, 3] or destino not in [1, 2, 3]:
            print("Error: Solo existen las torres 1, 2 y 3.")
            continue
            
        if origen == destino:
            print("Error: La torre de origen y destino no pueden ser la misma.")
            continue
            
        if torres[origen].vacia():
            print(f"Error: La torre {origen} está vacía. No hay disco para tomar.")
            continue
            
        disco_a_mover = ver_tope(torres[origen])
        disco_destino = ver_tope(torres[destino])
        
        # Validamos que no se apile un disco mayor sobre uno menor
        if disco_a_mover is not None and disco_destino is not None and disco_a_mover > disco_destino:
            print(f"Jugada imposible: No podés poner el disco {disco_a_mover} sobre el {disco_destino}.")
            continue
            
        # EJECUCIÓN DEL MOVIMIENTO
        # Si pasó todos los filtros de error, movemos la pieza
        disco = torres[origen].suprimir()
        torres[destino].insertar(disco)
        jugadas_realizadas += 1
        print(f"Éxito! Moviste el disco {disco} de la torre {origen} a la {destino}.")

    print("FELICITACIONES! Completaste el juego")
    print(f"Número de jugadas realizadas: {jugadas_realizadas}")
    print(f"Número mínimo de jugadas posibles: {jugadas_minimas}")

if __name__ == "__main__":
    jugar_hanoi()