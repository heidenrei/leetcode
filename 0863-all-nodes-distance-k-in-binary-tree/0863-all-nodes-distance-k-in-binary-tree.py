# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        nroot = None
        root.parent = None
        def go(node):
            nonlocal nroot
            if node == target:
                nroot = node
            if node.left:
                node.left.parent = node
                go(node.left)
            if node.right:
                node.right.parent = node
                go(node.right)
        go(root)
        
        if not nroot:
            return []
                
        def go(node, d, prev):
            if d == k:
                ans.append(node.val)
            if node.left and node.left != prev:
                go(node.left, d+1, node)
            if node.right and node.right != prev:
                go(node.right, d+1, node)
            if node.parent and node.parent != prev:
                go(node.parent, d+1, node)
            
        go(nroot, 0, None)
        return ans