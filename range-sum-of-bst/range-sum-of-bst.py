# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        res = 0
        
        def go(node):
            nonlocal res
        
            if node.val >= low and node.val <= high:
                res += node.val
            
            if node.left:
                go(node.left)
            if node.right:
                go(node.right)
                
        go(root)
        
        return res