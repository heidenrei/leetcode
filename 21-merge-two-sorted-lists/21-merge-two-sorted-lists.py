# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while l1:
            nums.append(l1.val)
            l1 = l1.next
        while l2:
            nums.append(l2.val)
            l2 = l2.next
        if not nums:
            return None
        nums.sort()
        head = ListNode(nums[0])
        og = head
        for x in nums[1:]:
            head.next = ListNode(x)
            head = head.next
            
        return og