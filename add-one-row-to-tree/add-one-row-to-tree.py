# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, left=root)
        def go(node, level):
            if not node:
                return
            
            tmp = node.left
            if level + 1 == d:
                node.left = TreeNode(v, left=tmp)

            go(node.left, level+1)
                
            tmp = node.right
            if level + 1 == d:
                node.right = TreeNode(v, right=tmp)

            go(node.right, level+1)
                
                
        go(root, 1)
        
        return root