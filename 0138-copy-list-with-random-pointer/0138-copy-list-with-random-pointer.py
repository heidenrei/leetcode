class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr = head
        
        newHead = Node(-1)
        copyCurrent = newHead
        
        lookup = {}
        
        while curr is not None:
            newNode = Node(curr.val)
            copyCurrent.next = newNode
            
            lookup[curr] = newNode
            
            copyCurrent = copyCurrent.next
            curr = curr.next
            
        curr = head
        copyCurrent = newHead.next
        
        while curr is not None:
            if curr.random is not None:
                copyCurrent.random = lookup[curr.random]
            curr = curr.next
            copyCurrent = copyCurrent.next
            
        return newHead.next