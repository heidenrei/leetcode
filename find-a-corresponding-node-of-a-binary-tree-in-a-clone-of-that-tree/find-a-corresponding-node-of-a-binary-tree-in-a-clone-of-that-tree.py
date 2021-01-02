# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans = []
        has_ans = False
        
        def go(node):
            nonlocal has_ans
            if not node or has_ans:
                return
            if node.val == target.val:
                ans.append(node)
                has_ans = True
            
            if node.left:
                go(node.left)
            if node.right:
                go(node.right)
                
        go(cloned)
                
        return ans[0]
