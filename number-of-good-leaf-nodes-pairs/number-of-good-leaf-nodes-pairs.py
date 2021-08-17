# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0
        
        def go(node):
            nonlocal ans
            out = []
            left = []
            right = []
            if node.left:
                left += [x+1 for x in go(node.left)]
            if node.right:
                right += [x+1 for x in go(node.right)]
            
            for x in left:
                for y in right:
                    if x + y <= distance:
                        ans += 1
            
            out += left
            out += right
            
            if not node.left and not node.right:
                out.append(0)
                
            return out
        
        go(root)
        
        return ans