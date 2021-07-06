# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def go(first, last):
            #print(first, last)
            ans = []
            for root in range(first, last+1):
                for left in go(first, root-1):
                    for right in go(root+1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        ans.append(node)
                        
            return ans or [None]
        
        return go(1, n)
            