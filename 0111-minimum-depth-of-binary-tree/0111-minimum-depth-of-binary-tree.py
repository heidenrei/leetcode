# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        @cache
        def go(node):
            if not node.left and not node.right:
                return 1
            ans = inf
            if node.left:
                ans = go(node.left) + 1
            if node.right:
                ans = min(ans, go(node.right) + 1)
            return ans
        return go(root) if root else 0