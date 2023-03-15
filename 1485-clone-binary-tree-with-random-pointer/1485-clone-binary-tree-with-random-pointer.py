# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        cnode = NodeCopy()
        if not root:
            return None
        s = defaultdict(NodeCopy)
        s[root] = cnode
        def go(node, cnode):
            cnode.val = node.val
            if node.random and node.random not in s:
                cnode.random = NodeCopy()
                #s.add(node.random)
                s[node.random] = cnode.random
                go(node.random, cnode.random)
            elif node.random:
                cnode.random = s[node.random]
            if node.left and node.left not in s:
                cnode.left = NodeCopy()
                #s.add(node.left)
                s[node.left] = cnode.left
                go(node.left, cnode.left)
            elif node.left:
                cnode.left = s[node.left]
                
            if node.right and node.right not in s:
                cnode.right = NodeCopy()
                #s.add(node.right)
                s[node.right] = cnode.right
                go(node.right, cnode.right)
            elif node.right:
                cnode.right = s[node.right]
                
        go(root, cnode)
        return cnode