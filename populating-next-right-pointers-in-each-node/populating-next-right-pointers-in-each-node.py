
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        prev = root
        curr = root.left
        
        while curr is not None:
            head = prev
            while prev is not None:
                curr.next = prev.right
                curr = curr.next

                prev = prev.next

                if prev is not None:
                    curr.next = prev.left
                    curr = curr.next
            prev = head.left
            curr = prev.left
                
        return root