# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        d = defaultdict(list)
        
        def go(node, level, val):
            
            d[level].append(val)
            
            if node.left:
                go(node.left, level+1, val*2)
            if node.right:
                go(node.right, level+1, val*2+1)
                
        go(root, 1, 0)
        
        best = 0
        
        for k, v in d.items():
            v.sort()
            if v[-1] - v[0] > 0:
                best = max(best, v[-1] - v[0])
            
        return best + 1