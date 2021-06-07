import bisect

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        vals = []
        pfs_vals = []
        
        def go(node):
            if not node:
                return
            
            vals.append(node.val)
            
            if node.left:
                go(node.left)
                
            if node.right:
                go(node.right)
        
        go(root)
        
        vals.sort()
        pfs = list(accumulate(vals))
        
        def go(node):
            if not node:
                return
            
            node.val += pfs[-1] - pfs[bisect.bisect_left(vals, node.val)]
            
            if node.left:
                go(node.left)
            if node.right:
                go(node.right)
        
        go(root)
        
        return root