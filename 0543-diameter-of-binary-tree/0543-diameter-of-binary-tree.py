class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        if not root:
            return 0
        def go(node):
            left = right = 0
            if node.left:
                left = go(node.left)
            if node.right:
                right = go(node.right)
                
                
            nonlocal best
            best = max(best, left + right)
                
            return max(left, right)+1
        
        go(root)
        return best