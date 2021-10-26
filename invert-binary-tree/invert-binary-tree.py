# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def go(node):
            if not node:
                return

            r = node.right
            l = node.left
            node.left = r
            node.right = l
            go(node.left)
            go(node.right)
        go(root)
        return root