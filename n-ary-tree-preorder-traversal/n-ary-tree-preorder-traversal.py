class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def go(node):
            if not node:
                return
            ans.append(node.val)

            for child in node.children:
                go(child)
        
        ans = []
        go(root)
        return ans