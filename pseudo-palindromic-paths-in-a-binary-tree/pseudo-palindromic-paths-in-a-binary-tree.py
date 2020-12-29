# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        cnt = 0
        
        def go(node, path, d):
            d += 1
            path ^= (1 << node.val)
                
            if node.left:
                go(node.left, path, d)
                
            if node.right:
                go(node.right, path, d)
            
            if not node.left and not node.right:
                nonlocal cnt
                cnt += not path or (d & 1 and math.log(path, 2) % 1 == 0)
                
        go(root, 0, 0)
        
        return cnt
