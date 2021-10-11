# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        if not root:
            return 0
        def go(node):
            left = right = 0
            if node.left:
                left = go(node.left)
            if node.right:
                right = go(node.right)
                
                
            nonlocal best
            best = max(best, left + right)
                
            return max(left, right)+1
        
        go(root)
        return best