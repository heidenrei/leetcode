class Solution:
    def countNodes(self, root: TreeNode) -> int:
        cnt = 0
        
        def go(node):
            nonlocal cnt
            if not node:
                return
            
            cnt += 1
            
            if node.left:
                go(node.left)
                
            if node.right:
                go(node.right)
                
        go(root)
        
        return cnt