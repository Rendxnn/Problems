class Solution:
    def maxProfit(self, prices) -> int:
        left = 0
        right = 0
        profit = 0
        while right < len(prices):
            current = prices[right] - prices[left]
            if current > profit:
                profit = current
            if prices[left] > prices[right]:
                left = right
            right += 1
        return profit


print(Solution().maxProfit([7, 6, 4, 3, 1]))
