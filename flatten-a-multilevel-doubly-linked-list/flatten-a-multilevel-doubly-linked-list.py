"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        ans = []
        def go(node):
            ans.append(node.val)
            if node.child:
                go(node.child)
            if node.next:
                go(node.next)

        go(head)
        
        og = Node(ans[0])
        curr = og
        prev = None
        for num in ans[1:]:
            curr.next = Node()
            prev = curr
            curr = curr.next
            curr.prev = prev
            curr.val = num
        
        return og