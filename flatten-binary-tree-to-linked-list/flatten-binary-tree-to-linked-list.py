# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        pre_order = []
        
        def go(node):
            if not node:
                return
            
            pre_order.append(node.val)
            go(node.left)
            go(node.right)
        
        go(root)
        if not pre_order:
            return
        print(pre_order)
        
        for i in range(len(pre_order)-1):
            root.val = pre_order[i]
            root.left = None
            root.right = TreeNode()
            root = root.right
            
        root.val = pre_order[-1]