class Solution:
    def jump(self, nums):
        print(nums)
        dic = {}
        ans = 0
        for index, num in enumerate(nums):
            for i in range(num + 1):
                if index + i >= len(nums):
                    break
                if index + i in dic:
                    dic[index + i] += [index]
                else:
                    dic[index + i] = [index]

        current = len(nums) - 1
        while min(dic[current]) != current:
            ans += 1
            current = min(dic[current])
        return ans


print(Solution.jump(Solution, [2, 3, 0, 1, 4]))