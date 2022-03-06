# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = 0
        def dfs(x, level):
            if not x:
                return
            nonlocal height
            
            if level > height:
                height = level
            dfs(x.left, level+1)
            dfs(x.right, level+1)
        dfs(root, 1)
        print(height)
        ans = [['' for x in range(2**(height)-1)] for y in range(height)]
        def go(node, i, j):
            if i < len(ans) and 0 <= j < len(ans[0]):
                ans[i][j] = str(node.val)
            if node.left:
                go(node.left, i+1, j-2**(height-i-2))
            if node.right:
                go(node.right, i+1, j+2**(height-i-2))
                
        go(root, 0, len(ans[0])//2)
        return ans