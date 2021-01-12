# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        one = []
        two = []
        
        while l1:
            one.append(str(l1.val))
            l1 = l1.next
            
        while l2:
            two.append(str(l2.val))
            l2 = l2.next
            
        one.reverse()
        two.reverse()
        
        one = int(''.join(one))
        two = int(''.join(two))
        
        total = str(one + two)
        
        total = total[::-1]
        
        head = ListNode(total[0])
        og = head
        for i in range(1, len(total)):
            head.next = ListNode(total[i])
            head = head.next
            
        return og
