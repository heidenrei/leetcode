# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def go(node):
            right = False
            left = False
            
            if node.left:
                left = go(node.left)
                
            if node.right:
                right = go(node.right)
                
            if node.val == 1:
                return True
                
            if not right and not left:
                node.val = -1
​
            return left or right
                
        def prune(node):
            if not node:
                return
            
            if node.left and node.left.val == -1:
                node.left = None
            if node.right and node.right.val == -1:
                node.right = None
                
            if node.left:
                prune(node.left)
                
            if node.right:
                prune(node.right)
        
        go(root)
        prune(root)
        
        return root if root.val != -1 else None
​
