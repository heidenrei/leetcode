# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
            
        N = len(nums)
        best = -inf
        for i in range(N//2, N):
            tmp = nums[i] + nums[-i-1]
            
            if tmp > best:
                best = tmp
                
        return best