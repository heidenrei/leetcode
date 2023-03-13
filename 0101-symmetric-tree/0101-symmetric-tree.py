# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def go(node1, node2):
            good = node1.val == node2.val
            if not ((node1.left and node2.right and go(node1.left, node2.right)) or (not node1.left and not node2.right)):
                good = False
            
            if not ((node2.left and node1.right and go(node2.left, node1.right)) or (not node2.left and not node1.right)):
                good = False
            return good
        
        return go(root, root)