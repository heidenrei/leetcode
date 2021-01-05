# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        d = defaultdict(int)
        og = head
        while head:
            d[head.val] += 1
            head = head.next
            
        prev = None
        head = og
        
        while head and d[head.val] != 1:
            head = head.next
        
        if head == None:
            return None
        
        og = head
        prev = None
        
        while head:
            if d[head.val] != 1:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
​
        return og
