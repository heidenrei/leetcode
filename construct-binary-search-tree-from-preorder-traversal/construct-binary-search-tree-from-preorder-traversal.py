class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        
        for i in range(1, len(preorder)):
            if preorder[i] > root.val:
                root.left = self.bstFromPreorder(preorder[1:i])
                root.right = self.bstFromPreorder(preorder[i:])
                return root
        else:
            root.left = self.bstFromPreorder(preorder[1:])
        return root