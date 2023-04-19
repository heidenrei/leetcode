# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def go(node):
            ll, lr, rl, rr = 0, 0, 0, 0
            if node.left:
                ll, lr = go(node.left)
            if node.right:
                rl, rr = go(node.right)
            nonlocal ans
            tmp = max(lr,rl)+1
            if tmp > ans:
                ans = tmp
            return lr+1, rl+1
        go(root)
        return ans-1
            