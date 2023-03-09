# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = head
        s = head
        
        while 1:
            if f is None:
                break
            f = f.next
            if f is None:
                break
            f = f.next
            s = s.next
            
            if f == s:
                break
                
        if f is None:
            return None
        
        s = head
        while f != s:
            f = f.next
            s = s.next
            
            if f == s:
                break
                
        
        return f