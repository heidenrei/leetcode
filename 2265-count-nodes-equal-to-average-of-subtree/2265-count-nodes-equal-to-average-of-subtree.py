class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def go(node):
            cnt = 1
            s = node.val
            if node.left:
                lc, ls = go(node.left)
                cnt += lc
                s += ls
            if node.right:
                rc, rs = go(node.right)
                cnt += rc
                s += rs
            nonlocal ans
            if node.val == s//cnt:
                ans += 1
            
            return cnt, s
        go(root)
        return ans