class Solution:
    def canPlaceFlowers(self, flowerbed,  n) -> bool:
        for i in range(len(flowerbed)):
            print(flowerbed)
            if n == 0:
                return True
            if i - 1 <= 0 and i + 1 < len(flowerbed):
                if flowerbed[i - 1] == flowerbed[i + 1] == flowerbed[i] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif flowerbed == 0:
                if flowerbed[i + 1] == flowerbed[i]:
                    n -= 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i - 1] == flowerbed[i] == 0:
                    n -= 1
                    flowerbed[i] = 1
        return n == 0


print(Solution.canPlaceFlowers(Solution, [1,0,0,0,1], 1))