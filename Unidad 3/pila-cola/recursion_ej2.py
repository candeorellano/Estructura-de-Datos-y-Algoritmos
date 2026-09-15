from pila_secuencial import Pila

def factorial_simulado(n):
    if n == 0:
        return 1

    pila_recursiva = Pila(n)

    for i in range(n, 0, -1):
        pila_recursiva.insertar(i)

    resultado = 1

    while pila_recursiva.vacia() is False:
        valor_actual = pila_recursiva.suprimir()
        resultado = resultado * valor_actual

    return resultado

if __name__ == "__main__":
    num = int(input("Ingrese el numero del que desea calcular el factorial: "))
    print(f"El factorial del numero {num} es: {factorial_simulado(num)}")