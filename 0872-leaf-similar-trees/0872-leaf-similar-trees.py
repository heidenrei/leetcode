# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leavs1 = []
        leavs2 = []
        
        def go1(node):
            if not node.left and not node.right:
                leavs1.append(node.val)
            if node.left:
                go1(node.left)
            if node.right:
                go1(node.right)
        if root1:
            go1(root1)
        def go2(node):
            if not node.left and not node.right:
                leavs2.append(node.val)
            if node.left:
                go2(node.left)
            if node.right:
                go2(node.right)
        if root2:
            go2(root2)
        return leavs1 == leavs2