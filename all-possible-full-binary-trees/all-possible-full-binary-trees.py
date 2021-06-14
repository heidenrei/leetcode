# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if not n & 1:
            return []
        
        @cache
        def go(x):
            if x == 1:
                return [TreeNode(0)]
            
            ans = []
            
            for i in range(1, x, 2):
                l = go(i)
                r = go(x - i - 1)
                for j in l:
                    for k in r:
                        ans.append(TreeNode(0, j, k))
                       
            return ans
                                   
        return go(n)