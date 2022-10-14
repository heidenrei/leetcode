# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        og = head
        while head:
            nums.append(head.val)
            head = head.next
            
        m = len(nums) // 2
        nums = nums[:m] + nums[m+1:]
        N = len(nums)
        if N == 0:
            return None
        head = ListNode(nums[0])
        i = 1
        og = head
        while i < N:
            head.next = ListNode(nums[i])
            head = head.next
            i += 1
            
        return og