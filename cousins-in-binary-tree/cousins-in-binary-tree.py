# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        d = defaultdict(list)
        
        def go(node, prev, level):
            if not node:
                return
            
            nonlocal d
            d[node.val] = [prev, level]
            
            if node.left:
                go(node.left, node.val, level+1)
            if node.right:
                go(node.right, node.val, level+1)
                
        go(root, None, 0)
        
        return d[x][0] != d[y][0] and d[x][1] == d[y][1]
                
        
