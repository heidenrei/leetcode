# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from sortedcontainers import SortedList

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        sl = SortedList()
        
        def go(node):
            sl.add(node.val)
            
            if node.left:
                go(node.left)
            if node.right:
                go(node.right)
                
        go(root)
        best = math.inf
        for i in range(1, len(sl)):
            best = min(best, sl[i] - sl[i-1])
            
        return best