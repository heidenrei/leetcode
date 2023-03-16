# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[0])
        
        node = postorder.pop()
        idx = inorder.index(node)
        node = TreeNode(node)
        
        node.right = self.buildTree(inorder[idx+1:], postorder)
        node.left = self.buildTree(inorder[:idx], postorder)
        
        return node