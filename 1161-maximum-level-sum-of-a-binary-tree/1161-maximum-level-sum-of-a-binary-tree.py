# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(int)
        def go(x, depth):
            d[depth] += x.val
            if x.left:
                go(x.left, depth+1)
            if x.right:
                go(x.right, depth+1)
        go(root, 1)
        v = max(d.values())
        for k in sorted(d.keys()):
            if d[k] == v:
                return k
            