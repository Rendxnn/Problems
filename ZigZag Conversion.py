def convert(s: str, numRows: int):
    matrix = ['' for _ in range(numRows)]
    letter = 0
    i = 0
    if numRows == 1:
        return s
    while True:
        while i < len(matrix):
            if letter >= len(s):
                print(matrix)
                return ''.join(matrix)
            matrix[i] += s[letter]
            letter += 1
            i += 1
        i -= 2
        while i >= 0:
            if letter >= len(s):
                print(matrix)
                return ''.join(matrix)
            matrix[i] += s[letter]
            letter += 1
            i -= 1
        i += 2


print(convert('PAYPALISHIRING', 3))