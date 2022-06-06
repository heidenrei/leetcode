# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ans = None
        og_A = headA
        
        
        while headA:
            headA.val *= -1 
            headA = headA.next
            
        while headB:
            if headB.val < 0:
                headB.val *= -1
                ans = headB
                break
            headB = headB.next

        headA = og_A
            
        while headA:
            if headA.val < 0:
                headA.val *= -1 
            headA = headA.next
            
        return ans