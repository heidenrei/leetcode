# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        og = head
        cnt = 1
        prev = None
        while head:
            if cnt == k:
                first = head
                first_prev = prev
            prev = head
            head = head.next
            cnt += 1
            
        target_cnt = cnt - k
        
        head = og
        
        cnt = 1
        prev = None
        while head:
            if cnt == target_cnt:
                second = head
                second_prev = prev
            prev = head
            head = head.next
            cnt += 1
                
        if second == first:
            return og
        elif k == 1:
            if cnt == 3:
                second.next = first
                first.next = None
                return second
            else:
                second.next = og.next
                second_prev.next = first
                first.next = None
                return second
        
        elif k == cnt - 1:
            if cnt == 3:
                first, second = second, first
                second.next = first
                first.next = None
                return second
            else:
                first.next = og.next
                first_prev.next = second
                second.next = None
                return first
        
        
        elif first.next == second:
            first_prev.next = second
            tmp = second.next
            second.next = first
            first.next = tmp
            return og
​
        else:
            # print(second.val)
            # print(second_prev.val)
​
            first_prev.next = second
            tmp = second.next
​
            second.next = first.next
​
            second_prev.next = first
            first.next = tmp
​
            return og
            
        
