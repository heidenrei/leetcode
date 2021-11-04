class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        def go(root, isleft):
            nonlocal res
            if not root:
                return
            if root.left:
                go(root.left, True)
            if root.right:
                go(root.right, False)
            if not root.left and not root.right and isleft:
                res += root.val
        go(root, False)
        return res