# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        og = head
        
        num_nodes = 1
        
        while head.next:
            head = head.next
            num_nodes += 1        
        
        
        
        head = og
        
        if n == num_nodes:
            if og.next:
                return og.next
            else:
                return None
        
        idx = 0
        while head and head.next:
            if idx == num_nodes - n - 1:
                if head.next.next:
                    head.next = head.next.next
                else:
                    head.next = None
                    
            idx += 1
            head = head.next
            
        
        return og  