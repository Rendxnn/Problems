class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        left, right = 0, len(nums) - 1
        last = 'left'
        while left != right:
            leftin = left + 1
            rightin = right - 1
            while leftin < rightin:
                if nums[left] + nums[right] + nums[leftin] + nums[rightin] == target:
                    ans.append([nums[left], nums[right], nums[leftin], nums[rightin]])
                    leftin += 1
                elif nums[left] + nums[right] + nums[leftin] + nums[rightin] > target:
                    rightin -= 1
                else:
                    leftin += 1
            if last == 'left':
                last = 'right'
                right -= 1
            else:
                last = 'left'
                left += 1
        return set(ans)


print(Solution.fourSum(Solution, [1,0,-1,0,-2,2], 0))