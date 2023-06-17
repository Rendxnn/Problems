# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def insertBalanced(root, num):
            current = root
            while True:
                if current.val < num:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(num)
                        return
                else:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(num)
                        return

        middle = len(nums) // 2
        left = middle - 1
        right = middle + 1

        root = TreeNode(nums[middle])

        while True:
            if 0 <= left:
                insertBalanced(root, nums[left])
                left -= 1
            if right < len(nums):
                insertBalanced(root, nums[right])
                right += 1
            if not right < len(nums) and not left >= 0:
                return root
