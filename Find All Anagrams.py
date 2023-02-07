def findAnagrams(s: str, p: str):
    letters = {}
    for letter in p:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    def is_anagram(substring):
        dic = letters.copy()
        print(substring, dic)
        for letter in substring:
            if letter not in dic or dic[letter] <= 0:
                return False
            else:
                dic[letter] -= 1
        for i in dic:
            if dic[i] != 0:
                return False
        return True

    i = 0
    ans = []
    last = False
    while i <= len(s) - len(p):
        if i > 0 and s[i - 1] == s[i + len(p) - 1] and last:
            ans.append(i)
        elif is_anagram(s[i:i + len(p)]):
            last = True
            ans.append(i)
        else:
            last = False
        i += 1
    return ans


print(findAnagrams('abab', 'ab'))