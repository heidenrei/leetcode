class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        ans = 0
        def go(node, pfs, d):
            tmp = defaultdict(int)
            for k, v in d:
                tmp[k] = v
            d = tmp
            curr = pfs + node.val
            
            nonlocal ans
            ans += d[curr - targetSum]
            d[curr] += 1
            d = tuple([(k, v) for k, v in d.items()])
            
            if node.left:
                go(node.left, curr, d)
            if node.right:
                go(node.right, curr, d)
            
        go(root, 0, tuple([(0, 1)]))
        
        return ans
            