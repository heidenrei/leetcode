import bisect

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        nums = []
        
        def go(node):
            nums.append(node.val)
            if node.left:
                go(node.left)
            if node.right:
                go(node.right)
        
        go(root)
        
        nums.sort(reverse=True)
        
        A = list(accumulate(nums))
        
        d = {k: v for k, v in zip(nums, A)}
        
        def go2(node):
            idx = bisect.bisect_left(A, node.val)
            node.val = d[node.val]
            if node.left:
                go2(node.left)
            if node.right:
                go2(node.right)
                
        go2(root)
        return root