# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        def go(node, path, sumi):
            path += '_' + str(node.val)
            sumi += node.val
            
            if node.left:
                go(node.left, path, sumi)
            if node.right:
                go(node.right, path, sumi)
                
            if not node.left and not node.right and sumi == targetSum:
                ans.append(path)
        ans = []
        go(root, '', 0)
                
        ans = [x.split('_')[1:] for x in ans]
        
        return ans