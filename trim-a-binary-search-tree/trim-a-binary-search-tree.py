# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        fakeRoot = TreeNode(float('-inf'))
        fakeRoot.right = root
        l = 0
        r = 1
        
        
        def go(parent, child, node):
            if not node:
                return None
            

            go(node, l, node.left)
            go(node, r, node.right)
            if not (low <= node.val <= high):
                if node.left is not None and low <= node.left.val <= high:
                    if child == l:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    if child == l:
                        parent.left = node.right
                    else:
                        parent.right = node.right
            
        go(fakeRoot, r, fakeRoot.right)
                    
        return fakeRoot.right