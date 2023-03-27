def winner(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]:
                n = matrix[i][j]
                if i + 1 < len(matrix) and j + 1 < len(matrix) and matrix[i + 1][j] == n and matrix[i + 1][j + 1] == n:
                    return False, n
                if i - 1 >= 0 and j + 1 < len(matrix) and matrix[i][j + 1] == n and matrix[i - 1][j] == n:
                    return False, n
                if i - 1 >= 0 and j - 1 >= 0 and matrix[i][j - 1] == n and matrix[i - 1][j - 1] == n:
                    return False, n
    return True, 0


def find_best_move(matrix, turn, score=0):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            win, player = winner(matrix)
            if win:
                if player == turn:
                    return 10
                else:
                    return -10
            if not matrix[i][j]:
                copia = [fila.copy() for fila in matrix]
                copia[i][j] = turn
