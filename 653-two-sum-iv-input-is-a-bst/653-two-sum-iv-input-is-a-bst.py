# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        vals = []
        
        def go(node):
            vals.append(node.val)
            if node.left:
                go(node.left)
            if node.right:
                go(node.right)
                
                
        go(root)
        
        seen = set()
        
        for x in vals:
            if target - x in seen:
                return True
            
            seen.add(x)
            
        return False