# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        
        if not t2:
            return t1
        
        def go(node1, node2):
            if not node1:
                return
            
            node1.val = node1.val + node2.val
            
            if node2.left and not node1.left:
                node1.left = TreeNode(0)
                
            if node2.right and not node1.right:
                node1.right = TreeNode(0)
            
            if node1.left and not node2.left:
                node2.left = TreeNode(0)
                
            if node1.right and not node2.right:
                node2.right = TreeNode(0)
            
            if node1.left:
                go(node1.left, node2.left)
                
            if node1.right:
                go(node1.right, node2.right)
                
        go(t1, t2)
​
        return t1
