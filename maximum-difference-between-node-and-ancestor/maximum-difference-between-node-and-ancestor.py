class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ans = 0
        
        if not root:
            return ans
        
        maxi = root.val
        mini = root.val
        
        
        def go(node, maxi, mini):
            nonlocal ans
            if not node:
                return
            
            ans = max(ans, max(abs(node.val - mini), abs(node.val - maxi)))
            
            if node.left:
                go(node.left, max(maxi, node.val), min(mini, node.val))
            if node.right:
                go(node.right, max(maxi, node.val), min(mini, node.val))
                
        go(root, maxi, mini)
        
        return ans