import random
from colorama import Fore


def traverse_matrix(matrix):
    num_island = 1
    memo = {}
    cant_islas = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i, j) not in memo:
                cant_islas[num_island] = 0
                search_island(matrix, i, j, memo, num_island, cant_islas)
                if cant_islas[num_island] == 1:
                    del memo[(i, j)]
                    matrix[i][j] = random.randint(-5, -1)
                num_island += 1
    show_matrix(matrix, memo)
    construir_puentes(matrix, memo)


def show_matrix(matrix, memo):
    colors = {1: Fore.RED, 2: Fore.BLACK, 3: Fore.BLUE, 4: Fore.CYAN, 5: Fore.GREEN, 6: Fore.MAGENTA, 0: Fore.YELLOW}
    result = []
    for i in range(len(matrix)):
        renglon = []
        for j in range(len(matrix)):
            if (i, j) in memo:
                renglon.append(
                    (colors[memo[(i, j)]] if memo[(i, j)] in colors else colors[memo[(i, j)] % 5]) + str(matrix[i][j]))
            else:
                renglon.append(Fore.RESET + str(matrix[i][j]))
        linea = ''
        for num in renglon:
            linea += num + (' ' * (10 - len(num)))
        result.append(linea)
    for i in result:
        print(i)


def search_island(matrix, i, j, memo, num_island, cant_islas):
    pos = matrix[i][j]
    if (i, j) not in memo:
        memo[(i, j)] = num_island
        cant_islas[num_island] += 1
        if j + 1 < len(matrix):
            neighbor_right = matrix[i][j + 1]
            if neighbor_right == pos + 1 or neighbor_right == pos - 1:
                search_island(matrix, i, j + 1, memo, num_island, cant_islas)
        if i + 1 < len(matrix):
            neighbor_down = matrix[i + 1][j]
            if neighbor_down == pos + 1 or neighbor_down == pos - 1:
                search_island(matrix, i + 1, j, memo, num_island, cant_islas)
        if j - 1 >= 0:
            neighbor_left = matrix[i][j - 1]
            if neighbor_left == pos + 1 or neighbor_left == pos - 1:
                search_island(matrix, i, j - 1, memo, num_island, cant_islas)


def construir_puentes(matrix, islas):
    caminos = buscar_puentes(matrix, islas)
    contador_puente = 0
    for camino in caminos:
        visitados = {}
        x_actual, y_actual = camino[0]
        x_destino, y_destino = camino[1]
        contador_puente += 1
        while (x_actual, y_actual) != (x_destino, y_destino):
            mejor_valor, mejor_opcion = float('inf'), None
            for i in range(-1, 2, 2):
                if 0 <= x_actual + i < len(matrix):
                    vecino = (x_actual + i, y_actual)
                    actual = (x_actual, y_actual)
                    if vecino not in islas or (vecino in islas and islas[vecino] == islas[(x_destino, y_destino)]):
                        casilla_vecina = matrix[x_actual + i][y_actual]
                        if casilla_vecina < 0:
                            valor_vecino = abs(x_destino - x_actual + i) + abs(y_destino - y_actual) + abs(casilla_vecina)
                        else:
                            valor_vecino = abs(x_destino - x_actual + i) + abs(y_destino - y_actual)
                        if valor_vecino < mejor_valor and vecino not in visitados:
                            mejor_valor = valor_vecino
                            mejor_opcion = vecino
                    if vecino in islas and actual in islas and islas[actual] == islas[vecino]:
                        casilla_vecina = matrix[x_actual + i][y_actual]
                        if casilla_vecina < 0:
                            valor_vecino = abs(x_destino - x_actual + i) + abs(y_destino - y_actual) + abs(
                                casilla_vecina)
                        else:
                            valor_vecino = abs(x_destino - x_actual + i) + abs(y_destino - y_actual)
                        if valor_vecino < mejor_valor and vecino not in visitados:
                            mejor_valor = valor_vecino
                            mejor_opcion = vecino

                if 0 <= y_actual + i < len(matrix):
                    vecino = (x_actual, y_actual + i)
                    actual = (x_actual, y_actual)
                    if vecino not in islas:
                        casilla_vecina = matrix[x_actual][y_actual + i]
                        if casilla_vecina < 0:
                            valor_vecino = abs(x_destino - x_actual) + abs(y_destino - y_actual + i) + abs(
                                casilla_vecina)
                        else:
                            valor_vecino = abs(x_destino - x_actual) + abs(y_destino - y_actual + i)
                        if valor_vecino < mejor_valor and vecino not in visitados:
                            mejor_valor = valor_vecino
                            mejor_opcion = vecino
                    if vecino in islas and actual in islas and islas[actual] == islas[vecino]:
                        casilla_vecina = matrix[x_actual + i][y_actual]
                        if casilla_vecina < 0:
                            valor_vecino = abs(x_destino - x_actual + i) + abs(y_destino - y_actual) + abs(
                                casilla_vecina)
                        else:
                            valor_vecino = abs(x_destino - x_actual + i) + abs(y_destino - y_actual)
                        if valor_vecino < mejor_valor and vecino not in visitados:
                            mejor_valor = valor_vecino
                            mejor_opcion = vecino
            print((x_actual, y_actual), mejor_opcion)

            if not mejor_opcion:
                break
            if mejor_opcion in visitados:
                break
            visitados[(x_actual, y_actual)] = 1

            x_actual, y_actual = mejor_opcion
            if (mejor_opcion[0], mejor_opcion[1]) not in islas:
                matrix[mejor_opcion[0]][mejor_opcion[1]] = contador_puente
        show_matrix(matrix, islas)


def buscar_puentes(matrix, memo):
    costos = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] < 0:
                costos[(i, j)] = matrix[i][j]

    numeros_islas = list(set(memo.values()))
    cant_islas = len(numeros_islas)
    islas_elegidas = {}
    caminos = []

    for num in range(cant_islas - 1):
        start_num = float('inf')
        start, end = None, None
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if 0 < matrix[i][j] < start_num and memo[(i, j)] not in islas_elegidas:
                    start_num = matrix[i][j]
                    start = (i, j)

        end_num = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if 0 < matrix[i][j] < end_num and memo[(i, j)] != memo[start] and memo[(i, j)] not in islas_elegidas:
                    end_num = matrix[i][j]
                    end = (i, j)

        islas_elegidas[memo[start]] = 1
        caminos.append((start, end))
    return caminos


m = [[45, 26, 17, 19, 39, 66, 65],
     [48, 34, 22, 36, 42, 67, 40],
     [49, 20, 13, 41, 53, 43, 56],
     [50, 51, 55, 10, 38, 33, 58],
     [37, 27, 18, 14, 35, 57, 11],
     [24, 52, 15, 54, 32, 16, 12],
     [25, 29, 47, 46, 31, 30, 21]]

traverse_matrix(m)
