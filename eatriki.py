def winner_triki(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][0] == matrix[i][1] == matrix[i][2] is not None:
                return True
            if matrix[0][j] == matrix[1][j] == matrix[2][j] is not None:
                return True
    if matrix[0][0] == matrix[1][1] == matrix[2][2] is not None:
        return True
    if matrix[2][0] == matrix[1][1] == matrix[0][2] is not None:
        return True


def winner(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            current = matrix[i][j]
            if not current:
                return False
            if i + 1 < len(matrix) and j + 1 < len(matrix) and matrix[i + 1][j + 1] == matrix[i + 1][j] == current:
                return True
            if i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1] == matrix[i][j - 1] == current:
                return True
            if i - 1 >= 0 and j + 1 < len(matrix) and matrix[i - 1][j] == matrix[i][j + 1] == current:
                return True
    return False


def minimax(matrix, turn, maximize):
    if maximize:
        value = -float('inf')
        move = (-1, - 1)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if not matrix[i][j]:
                    copy = [row.copy() for row in matrix]
                    copy[i][j] = turn
                    if winner_triki(copy):
                        return ((i, j), 10)
                    result = minimax(copy, 'X' if turn == 'O' else 'O', False)
                    if result[1] > value:
                        value = result[1]
                        move = (i, j)
        return (move, value) if move != (-1, - 1) else ((len(matrix) - 1, len(matrix) - 1), 0)
    else:
        value = float('inf')
        move = (-1, - 1)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if not matrix[i][j]:
                    copy = [row.copy() for row in matrix]
                    copy[i][j] = turn
                    if winner_triki(copy):
                        return ((i, j), -10)
                    result = minimax(copy, 'X' if turn == 'O' else 'O', True)
                    if result[1] < value:
                        value = result[1]
                        move = (i, j)
        return (move, value) if move != (-1, - 1) else ((len(matrix) - 1, len(matrix) - 1), 0)


def main():
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    while True:
        for row in board:
            print(row)
        pos = input('elija una posición para jugar: (fila columna) ')
        print()
        i, j = list(map(int, pos.split()))
        board[i][j] = 'X'
        if winner_triki(board):
            break
        pc = minimax(board, 'O', True)
        i, j = pc[0]
        board[i][j] = 'O'
        if winner_triki(board):
            break
    print('el juego ha finalizado')
    for row in board:
        print(row)


main()


triki = [['X', None, None],
         ['O', 'O', 'X'],
         ['X', None, None]]



