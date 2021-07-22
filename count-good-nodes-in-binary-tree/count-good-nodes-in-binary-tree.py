# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def go(node, maxi):
            maxi = max(maxi, node.val)
            if maxi <= node.val:
                nonlocal ans
                ans += 1
            if node.left:
                go(node.left, maxi)
            if node.right:
                go(node.right, maxi)
                
        go(root, -(10**4))
        
        return ans