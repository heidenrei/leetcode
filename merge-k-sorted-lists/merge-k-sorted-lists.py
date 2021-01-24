# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nums = []
        
        if not lists:
            return None
        
        idx = 0
        
        while idx < len(lists):
            if lists[idx] == None:
                lists = lists[:idx] + lists[idx+1:]
            else:
                idx += 1
        
        if not lists:
            return None
        
        for l in lists:
            head = l
            nums.append(head.val)
            while head:
                head = head.next
                if head:
                    nums.append(head.val)
​
                
        nums.sort()
        head = ListNode(nums[0])
        og = head
        for i in range(1, len(nums)):
            head.next = ListNode(nums[i])
            head = head.next
            
        return og
