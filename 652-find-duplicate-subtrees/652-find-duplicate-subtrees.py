# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        preo = []
        ans = []
        d = defaultdict(int)
        def go(node):
            if not node:
                return '#'
            path = ','.join([str(node.val), go(node.left), go(node.right)])
            d[path] += 1
            if d[path] == 2:
                ans.append(node)
            return path     
        go(root)
        return ans