class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1, 'a': 1, 's': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l': 1, 'ñ': 1, 'z': 1, 'x': 1, 'c': 1, 'v': 1, 'b': 1, 'n': 1, 'm': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '0': 1}
        translation = ''
        for char in s.lower():
            if char in valid:
                translation += char

        return translation == translation[::-1]

