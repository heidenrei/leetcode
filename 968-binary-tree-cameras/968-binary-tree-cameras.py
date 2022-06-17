class Solution:
    def minCameraCover(self, node: TreeNode) -> int:
        seen = set()

        def go(node):
            if not node:
                return True
            if not all([go(node.left), go(node.right)]): 
                seen.add(node)
            return node in seen or (node.left and node.left in seen) or (node.right and node.right in seen)

        if not go(node): 
            seen.add(node)
        
        return len(seen)