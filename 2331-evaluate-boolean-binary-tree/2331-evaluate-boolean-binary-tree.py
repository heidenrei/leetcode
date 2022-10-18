# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def go(node):
            if not node.left and not node.right:
                return node.val
            if node.val == 2:
                return go(node.left) | go(node.right)
            else:
                return go(node.left) & go(node.right)
        return go(root)