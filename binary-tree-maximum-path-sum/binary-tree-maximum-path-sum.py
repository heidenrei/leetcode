# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.maxval = root.val
        self.dfs(root)
        
        return self.maxval
        
    def dfs(self, root):
        if not root:
            return 0
        leftmax = self.dfs(root.left)
        rightmax = self.dfs(root.right)
        self.maxval = max(self.maxval, root.val+leftmax+rightmax)
        return max(root.val, root.val+max(leftmax, rightmax), 0)
