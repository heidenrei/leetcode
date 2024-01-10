# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        infected = None
        root.par = None
        
        def dfs(node):
            if node.val == start:
                nonlocal infected
                infected = node
            if node.left:
                node.left.par = node
                dfs(node.left)
            if node.right:
                node.right.par = node
                dfs(node.right)
                
        dfs(root)
                
        def go(node, prev):
            ans = 0
            if node.left and node.left != prev:
                ans = max(ans, go(node.left, node)+1)
            if node.right and node.right != prev:
                ans = max(ans, go(node.right, node)+1)
            if node.par is not None and node.par != prev:
                ans = max(ans, go(node.par, node)+1)
                
            return ans
        
        return go(infected, None)