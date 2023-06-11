# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        a = []
        def go(x):
            a.append(x.val)
            if x.left:
                go(x.left)
            if x.right:
                go(x.right)
        go(root)
        a.sort(key=lambda x: abs(target - x))
        return a[:k]