def diferenciaMatriz(matriz):
    def columnas(simbolo, i, j, respuesta):
        if i == len(matriz) - 1 and j == len(matriz) - 1:
            return respuesta
        elif j < len(matriz):
            if j % 2 != 0:
                if simbolo == '+':
                    respuesta += matriz[i][j]
                elif simbolo == '*':
                    respuesta *= matriz[i][j]
            return columnas(simbolo, i, j + 1, respuesta)
        elif i < len(matriz):
            return columnas(simbolo, i + 1, 0, respuesta)
        return respuesta

    def filas(simbolo, i, j, respuesta):
        if i == len(matriz) - 1 and j == len(matriz) - 1:
            return respuesta
        elif j < len(matriz):
            if i % 2 != 0:
                if simbolo == '+':
                    respuesta += matriz[i][j]
                elif simbolo == '*':
                    respuesta *= matriz[i][j]
            return columnas(simbolo, i, j + 1, respuesta)
        elif i < len(matriz):
            return columnas(simbolo, i + 1, 0, respuesta)

    filasImpares = filas('+', 0, 0, 0)
    columnasImpares = columnas('*', 0, 0, 1)
    diferencia = filasImpares - columnasImpares
    return diferencia


matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]



from functools import reduce


def comparar_listas(lista1, lista2):
    parejas_no_iguales = filter(lambda x: x[0] != x[1], zip(lista1, lista2))
    resultado = reduce(lambda acc, _: False, parejas_no_iguales, True)

    return resultado


a = ["hola", "como", "estas"]
b = ["hola", "como", "estas", "hoy"]

if comparar_listas(a, a):
    print("Las listas son iguales")
else:
    print("Las listas no son iguales")

if comparar_listas(a, b):
    print("Las listas son iguales")
else:
    print("Las listas no son iguales")


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Persistente:
    def __init__(self, head):
        self.head = head

    def buscar_Consecutivos(self):
        if self.head.next:
            if self.head.value in [self.head.next.value + 1, self.head.next.value - 1]:
                return True
            self.head = self.head.next
            return self.buscar_Consecutivos()
        return False


n1 = Node(1)
n2 = Node(2)
n3 = Node(5)
n4 = Node(3)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

persistente = Persistente(n1)
print(persistente.buscar_Consecutivos())
