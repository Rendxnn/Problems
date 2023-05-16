class Solution:
    def search(self, nums, target):
        left, right, mid = 0, len(nums) - 1, 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        return - 1


print(Solution.search(Solution, [-1,0,3,5,9,12], 9))