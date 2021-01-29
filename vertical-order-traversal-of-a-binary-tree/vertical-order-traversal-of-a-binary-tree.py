# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dx = defaultdict(list)
        dy = defaultdict(list)
        
        def go(node, x, y):
            if not node:
                return
            
            dx[x].append(node)
            dy[node] = y
            
            if node.left:
                go(node.left, x-1, y+1)
            if node.right:
                go(node.right, x+1, y+1)
                
        go(root, 0, 0)
        
        min_x = min(dx.keys())
        max_x = max(dx.keys())
        
        ans = []
                
        for key in range(min_x, max_x+1):
            ans.append(dx[key])
        
        ans = [sorted(x, key=lambda x: [dy[x], x.val]) for x in ans]
        
        ans = [[x.val for x in y] for y in ans]
                
        return ans