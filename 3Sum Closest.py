class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        left = 0
        right = len(nums) - 1
        closest = float('inf')
        print(nums)
        while left < right:
            mid = left + 1
            print(nums[left], nums[mid], nums[right], closest)
            while mid < right:
                current = nums[left] + nums[right] + nums[mid]
                print(nums[left], nums[mid], nums[right], closest)
                if current == target:
                    return current
                else:
                    closest = current
                mid += 1
            if closest > target:
                right -= 1
            elif closest < target:
                left += 1
        return closest


print(Solution.threeSumClosest(Solution, [0,3,97,102,200], 300))

# [-4, -1, 1, 2]
