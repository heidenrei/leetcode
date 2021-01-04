# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        ans = []
        
        while l1 and l2:
            if l1.val <= l2.val:
                ans.append(l1.val)
                l1 = l1.next
            else:
                ans.append(l2.val)
                l2 = l2.next
                
        while l1:
            ans.append(l1.val)
            l1 = l1.next
            
        while l2:
            ans.append(l2.val)
            l2 = l2.next
        
        tail = ListNode(ans[0])
        og = tail
        
        for i in range(1, len(ans)):
            tmp = ListNode(ans[i])
            tail.next = tmp
            tail = tail.next
            
        return og
