class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        d = defaultdict(int)
        
        def dfs(node, depth):
            d[depth] += node.val
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
                
        dfs(root, 0)
        
        max_depth = max([k for k in d.keys()])
        
        for k, v in d.items():
            if k == max_depth:
                return v