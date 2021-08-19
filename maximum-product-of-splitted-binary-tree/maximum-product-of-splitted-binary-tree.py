# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9+7
        
        def total(node):
            if node is None:
                return 0
            
            return node.val + total(node.left) + total(node.right)
        
        treeSum = total(root)
        best = 0
        
        def findMax(node):
            if node is None:
                return 0
            
            subtreeSum = node.val + findMax(node.left) + findMax(node.right)
            nonlocal best
            best = max(best, subtreeSum * (treeSum - subtreeSum))
            
            return subtreeSum
        
        findMax(root)
        
        return best % MOD