# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = None
        def go(node):
            nonlocal ans
            if not node or ans:
                return False
            
            left = False
            right = False
            
            if node.left:
                left = go(node.left)
            if node.right:
                right = go(node.right)
            
            #print(left, right)
            
            if (any([node == p, node == q]) and any([left, right])) or (left and right):
                ans = node
                return True
                
            return sum([node == p, node == q, left, right]) == 1
        
        go(root)
        return ans