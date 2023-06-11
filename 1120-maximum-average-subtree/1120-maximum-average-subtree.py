# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        ans = 0
        def go(x):
            s, c = x.val, 1
            if x.left:
                sl, cl = go(x.left)
                s += sl
                c += cl
            if x.right:
                sr, cr = go(x.right)
                s += sr
                c += cr
            
            nonlocal ans
            if s/c > ans:
                ans = s/c
            return s, c
        go(root)
        return ans
            