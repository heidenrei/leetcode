class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(None)
        def canRob(node):
            if not node:
                return 0
            
            rob = node.val + cantRob(node.left) + cantRob(node.right)
            
            dontrob = canRob(node.left) + canRob(node.right)
            
            return max(rob, dontrob)
        
        @lru_cache(None)
        def cantRob(node):
            if not node:
                return 0
            
            return canRob(node.left) + canRob(node.right)
        
        return canRob(root)