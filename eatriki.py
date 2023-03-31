def winner(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]:
                n = matrix[i][j]
                if i + 1 < len(matrix) and j + 1 < len(matrix) and matrix[i + 1][j] == n and matrix[i + 1][j + 1] == n:
                    return True, n
                if i - 1 >= 0 and j + 1 < len(matrix) and matrix[i][j + 1] == n and matrix[i - 1][j] == n:
                    return True, n
                if i - 1 >= 0 and j - 1 >= 0 and matrix[i][j - 1] == n and matrix[i - 1][j - 1] == n:
                    return True, n
    return False, 0


def find_best_move(matrix, turn, move, original_turn=None):
    for row in matrix:
        print(row)
    print()

    if not original_turn:
        original_turn = turn
    win, player = winner(matrix)
    best_value = None
    best_move = None
    if win:
        return move, -10 if turn == original_turn else 10
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not matrix[i][j]:
                matrix_copy = [row.copy() for row in matrix]
                matrix_copy[i][j] = turn
                best = find_best_move(matrix_copy, 'X' if turn == 'O' else 'O', (i, j), original_turn)
                print(best)
                if turn == original_turn:
                    if best_value and best[1] < best_value:
                        best_value = best[1]
                        best_move = best[0]
                    else:
                        best_value = best[1]
                        best_move = best[0]
                else:
                    if best_value and best[1] > best_value:
                        best_value = best[1]
                        best_move = best[0]
                    else:
                        best_value = best[1]
                        best_move = best[0]

    return best_move if best_move else move, 0


M = [['X', None, 'X', 'X'],
     ['X', 'O', 'O', 'O'],
     [None, 'X', 'O', 'X'],
     [None, 'O', 'X', 'X']]

print(find_best_move(M, 'X', None))
