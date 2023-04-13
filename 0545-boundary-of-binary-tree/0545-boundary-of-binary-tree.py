# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return [root.val]
        seen = set()
        leaves = []
        def go(node):
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.left:
                go(node.left)
            if node.right:
                go(node.right)
        go(root)
        
        leftb = []
        
        def left(node):
            if node.left or node.right:
                leftb.append(node.val)
            if node.left:
                left(node.left)
            if not node.left and node.right:
                left(node.right)
        
        if root.left:
            left(root.left)
        
        rightb = []
        
        def right(node):
            if node.left or node.right:
                rightb.append(node.val)
            if node.right:
                right(node.right)
            if node.left and not node.right:
                right(node.left)
        
        if root.right:
            right(root.right)
        
        # print(leftb)
        # print(leaves)
        # print(rightb)
        
        return [root.val] + leftb + leaves + rightb[::-1]
                    