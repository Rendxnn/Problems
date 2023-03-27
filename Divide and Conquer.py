def contar_matriz(matriz):
    maximo = 0
    indice = -1
    medio = len(matriz) // 2
    for fila in range(len(matriz)):
        if medio + fila < len(matriz):
            derecha = contar_fila(matriz[medio + fila])
            if derecha > maximo:
                maximo = derecha
                indice = medio + fila
        if medio - fila >= 0:
            izquierda = contar_fila(matriz[medio - fila])
            if izquierda > maximo:
                maximo = izquierda
                indice = medio - fila
    return indice


def contar_fila(fila):
    if len(fila) == 1:
        return fila[0]
    medio = len(fila) // 2
    return contar_fila(fila[medio:]) + contar_fila(fila[:medio])


ejemplo = [[1, 1, 1, 1],
           [1, 1, 0, 0],
           [0, 0, 0, 0],
           [1, 1, 1, 0]]
print(contar_matriz(ejemplo))
