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


def show_matrix(matrix, memo):
    colors = {1: Fore.RED, 2: Fore.BLACK, 3: Fore.BLUE, 4: Fore.CYAN, 5: Fore.GREEN, 6: Fore.MAGENTA, 0: Fore.YELLOW}
    result = []
    for i in range(len(matrix)):
        renglon = []

        for j in range(len(matrix)):
            if (i, j) in memo:
                renglon.append(
                    (colors[memo[(i, j)]] if memo[(i, j)] in colors else colors[memo[(i, j)] % 3]) + str(matrix[i][j]))
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


m = [[34, 24, 12, 11, 20],
     [33, 14, 13, 31, 18],
     [25, 15, 16, 19, 26],
     [21, 22, 32, 23, 27],
     [30, 10, 17, 29, 28]]

traverse_matrix(m)
