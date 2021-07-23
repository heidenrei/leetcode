# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def go(node):
            curr_has = node.val == 1
            left_has = False
            right_has = False
            if node.left:
                left_has = go(node.left)
            if node.right:
                right_has = go(node.right)
                
            if not left_has:
                node.left = None
            if not right_has:
                node.right = None
                
            return curr_has or left_has or right_has
        
        if go(root):
            return root
        else:
            return None