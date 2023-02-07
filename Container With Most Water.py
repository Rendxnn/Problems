class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left != right:
            if min(height[left], height[right]) * (right - left) > max_area:
                max_area = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


print(Solution.maxArea(Solution, [1,8,6,2,5,4,8,3,7]))