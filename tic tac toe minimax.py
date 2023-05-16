dic = {}


def minimax(triki, turn, maximizar):
    if maximizar:
        value = -float('inf')
    else:
        value = float('inf')

    move = (-1, -1)
    for i in range(len(triki)):
        for j in range(len(triki)):
            if not triki[i][j]:
                if tablero in dic:
                    return dic[ ]
                tablero = ''
                triki[i][j] = turn
                copy = []
                for row in triki:
                    copy.append(row.copy())
                    for x in row:
                        if x:
                            tablero += x
                        else:
                            tablero += '_'
                triki[i][j] = None
                if ganador(copy, i, j):
                    if maximizar:
                        dic[tablero] = 10
                        return (i, j), 10
                    else:
                        dic[tablero] = -10
                        return (i, j), -10
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                recursion = minimax(copy, turn, True if not maximizar else False)
                if recursion[1] >= value and maximizar:
                    value = recursion[1]
                    move = recursion[0]

                elif recursion[1] <= value and not maximizar:
                    value = recursion[1]
                    move = recursion[0]
    if move != (-1, -1):
        return move, value
    else:
        return (-1, -1), 0


def jugador_vs_pc():
    pass


def ganador(triki, i, j):
    current_position = triki[i][j]

    if i - 1 >= 0 and j - 1 >= 0 and triki[i][j - 1] == triki[i - 1][j - 1] == current_position:
        return True
    if i - 1 < len(triki) and j + 1 < len(triki) and triki[i - 1][j] == triki[i][j + 1] == current_position:
        return True
    if i + 1 < len(triki) and j + 1 < len(triki) and triki[i + 1][j] == triki[i + 1][j + 1] == current_position:
        return True
    return False


triki = [['X', None, None, None],
         ['X', None, None, None],
         [None, None, 'O', None],
         [None, 'O', None, None]]


def main():
    end_game = False
    while not end_game:

        for row in triki:
            print(row)
        print(f"mejor jugada: {minimax(triki, 'O', True)})")

        position = list(map(int, input("Ingrese fila columna: ").split()))
        triki[position[0]][position[1]] = "X"
        end_game = ganador(triki, position[0], position[1])
        if end_game:
            break
        maquina = minimax(triki, 'O', True)[0]
        triki[maquina[0]][maquina[1]] = 'O'
        end_game = ganador(triki, maquina[0], maquina[1])
        print(minimax(triki, 'O', True))
    for row in triki:
        print(row)


main()