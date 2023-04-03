# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def go(node):
            left = right = 0
            if node.left:
                left = go(node.left)
            if node.right:
                right = go(node.right)
            nonlocal res
            res += abs(left) + abs(right)
            #print(node.val, cnt, ans)
            return left + right + node.val - 1
        res = 0
        go(root)
        return res