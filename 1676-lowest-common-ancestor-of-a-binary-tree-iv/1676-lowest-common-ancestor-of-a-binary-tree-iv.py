# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        ret = None
        ansd = -inf
        node_vals = [node.val for node in nodes]
        def go(node, d):
            ans = 0 + (node.val in node_vals)
            if node.left:
                ans += go(node.left, d+1)
            if node.right:
                ans += go(node.right, d+1)
            nonlocal ansd, ret
            if ans == len(nodes) and d > ansd:
                ansd = d
                ret = node
            return ans
        
        go(root, 0)
        return ret