# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ansd = -inf
        ans = None
        def go(node, d):
            hasp = node == p
            hasq = node == q
            if node.left:
                lhasq, lhasp = go(node.left, d+1)
                hasp |= lhasp
                hasq |= lhasq
            if node.right:
                rhasq, rhasp = go(node.right, d+1)
                hasp |= rhasp
                hasq |= rhasq
            nonlocal ansd, ans
            if hasp & hasq & (ansd < d):
                ansd = d
                ans = node
            
            return hasq, hasp
        
        go(root, 0)
        return ans