# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def go(node):
            bestd = abs(node.val - target)
            bestv = node.val
            if node.left:
                leftd, leftv = go(node.left)
                if leftd <= bestd:
                    bestd = leftd
                    bestv = leftv
                
            if node.right:
                rightd, rightv = go(node.right)
                if rightd < bestd:
                    bestd = rightd
                    bestv = rightv
            return bestd, bestv
        ansd, ansv = go(root)
        return ansv
                