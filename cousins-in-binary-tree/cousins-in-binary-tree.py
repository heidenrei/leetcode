# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        d = defaultdict(list)
        p = defaultdict(int)
        
        q = [root]
        level = 0
        
        while q:
            tmp = []
            while q:
                node = q.pop()
                d[node.val].append(level)
                if node.left:
                    p[node.left.val] = node.val
                    tmp.append(node.left)
                if node.right:
                    p[node.right.val] = node.val
                    tmp.append(node.right)
            q = tmp
            level += 1
        
        return p[x] != p[y] and d[x] == d[y]