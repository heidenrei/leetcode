# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def go(rem):
            mid = rem[len(rem)//2]
            left = rem[:len(rem)//2]
            right = rem[len(rem)//2+1:]
            curr = TreeNode(mid)
            if left:
                curr.left = go(left)
            if right:
                curr.right = go(right)
                
            return curr
        
        return go(nums)