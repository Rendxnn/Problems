def checkInclusion(s1: str, s2: str) -> bool:
    chars = 'qwertyuiopasdfghjklzxcvbnm'
    dic = {}
    for index, char in enumerate(chars):
        dic[char] = index

    num1 = ''.join([f'{s1.count(char)}' for char in chars])
    i = 0
    while i <= len(s2) - len(s1):
        num2 = ''.join([f'{s2[i:i + len(s1)].count(char)}' for char in chars])
        print(num1, num2)
        if num1 == num2:
            return True
        i += 1
    return False


print(checkInclusion('a', 'ab'))


