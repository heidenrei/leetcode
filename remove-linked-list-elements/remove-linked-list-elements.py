# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = head
        prev = None

        while curr:
            if curr.val == val:
                if curr == head:
                    head = head.next
                    curr = head
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return head