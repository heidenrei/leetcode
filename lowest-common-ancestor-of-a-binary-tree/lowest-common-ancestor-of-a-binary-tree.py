# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        
        def go(node):
            
            x, y, z, a = False, False, False, False
            
            if node.left:
                x, y = go(node.left)
            if node.right:
                z, a = go(node.right)
            
            x = x or z
            y = y or a
            
            if node == p:
                x = True
                
            if node == q:
                y = True
            
            if x and y:
                nonlocal ans
                if not ans:
                    ans = node
            return [x, y]
                
        go(root)
        
        return ans