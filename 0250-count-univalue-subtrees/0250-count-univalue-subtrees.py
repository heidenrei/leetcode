# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        def go(x):
            vl = val = vr = x.val
            good = True
            if x.left:
                vl, gl = go(x.left)
                good &= gl
            if x.right:
                vr, gr = go(x.right)
                good &= gr
            if vl == val == vr and good:
                nonlocal ans
                ans += 1
            else:
                good = False
            return val, good
        go(root)
        return ans