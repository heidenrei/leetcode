# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.cnt = 0
        self.cnt2 = 0
        self.helper(head)
        return self.helper2(head)
        
    def helper(self, head):
        if not head:
            return
        self.cnt += 1
        return self.helper(head.next)

    def helper2(self, head):
        if not head:
            return
        midpoint = self.cnt // 2
        while self.cnt2 < midpoint:
            self.cnt2 += 1
            return self.helper2(head.next)
        return head