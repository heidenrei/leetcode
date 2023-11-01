# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        nodes = []
        ans = []
        
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        def dfs(root):
            if not root:
                return
            nodes.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            if not root.right and not root.left:
                return
        
        dfs(root)
        c = collections.Counter(nodes)
                
        maxi = 0
        
        for k, v in c.items():
            if v > maxi:
                maxi = v
        
        for k, v in c.items():
            if v == maxi:
                ans.append(k)
                
        return ans