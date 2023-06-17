class Solution:
    def findCircleNum(self, matrix):
        contador = 0
        provincias = {}
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i != j and matrix[i][j] == 1:
                    if i in provincias and j in provincias:
                        for provincia in provincias:
                            if provincias[provincia] == provincias[j]:
                                provincias[provincia] = provincias[i]
                        contador = max(provincias.values()) + 1
                    elif i in provincias:
                        provincias[j] = provincias[i]
                    elif j in provincias:
                        provincias[i] = provincias[j]
                    else:
                        provincias[i], provincias[j] = contador, contador
                        contador += 1
                elif i == j:
                    if i not in provincias:
                        provincias[i] = contador
                        contador += 1
        print(provincias)
        return len(set(provincias.values()))


print(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
