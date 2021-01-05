# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        univalue = root.val
        ans = True
        def go(node):
            if not node:
                return
            if node.val != univalue:
                nonlocal ans
                ans = False
            if node.left:
                go(node.left)
            if node.right:
                go(node.right)
                
        go(root)
        
        return ans
