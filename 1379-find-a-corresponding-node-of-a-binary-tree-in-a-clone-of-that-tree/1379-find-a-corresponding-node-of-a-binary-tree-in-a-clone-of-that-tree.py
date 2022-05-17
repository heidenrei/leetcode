# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans = None
        def go(node):
            if node.val == target.val:
                nonlocal ans
                ans = node
            if node.left:
                go(node.left)
            if node.right:
                go(node.right)
                
        go(cloned)
        return ans