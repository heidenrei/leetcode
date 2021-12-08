# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        sumi = 0
        
        def go(node):
            nonlocal sumi
            if not node:
                return 0
            
            left = go(node.left)
            right = go(node.right)
            
            sumi += abs(left - right)
            
            
            return left + right + node.val
        
    
        go(root)
        return sumi