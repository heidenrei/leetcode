# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = inf
        a = []
        def go(x):
            a.append(x.val)
            if x.left:
                go(x.left)
            if x.right:
                go(x.right)
        go(root)
        a.sort()
        for i in range(len(a)-1):
            ans = min(ans, a[i+1] - a[i])
        return ans