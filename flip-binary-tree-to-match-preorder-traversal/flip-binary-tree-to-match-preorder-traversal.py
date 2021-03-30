# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root, v: List[int]) -> List[int]:
        N = len(v)
        idx = 0
        possible = True
        swaps = []
        
        def preorder(node):
            if not node:
                return
            
            nonlocal idx
            if node.val != v[idx]:
                nonlocal possible
                possible = False
                return
            
            idx += 1
            
            if node.right is not None and node.right.val == v[idx] and node.left is not None:
                swaps.append(node.val)
                preorder(node.right)
                preorder(node.left)
            else:
                preorder(node.left)
                preorder(node.right)
                
        preorder(root)
        
        if possible:
            return swaps
        else:
            return [-1]