# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        best = 0
        @cache
        def go(node):
            ans = 1
            right_dec = right_asc = left_dec = left_asc = 0
            if node.left:
                if (node.left.val - node.val) == -1:
                    left_dec = go(node.left)[0]
                elif node.left.val - node.val == 1:
                    left_asc = go(node.left)[1]
                else:
                    go(node.left)
            if node.right:
                if (node.right.val - node.val) == -1:
                    right_dec = go(node.right)[0]
                elif node.right.val - node.val == 1:
                    right_asc = go(node.right)[1]
                else:
                    go(node.right)
            
            up = left_dec + right_asc + 1
            down = left_asc + right_dec + 1
            nonlocal best
            best = max(best, up, down)
                
            return max(left_dec, right_dec) + 1, max(left_asc, right_asc) + 1
            
        go(root)
        return best