# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        N = len(nodes)
        
        if not N & 1:
            first_half = nodes[1:N//2][::-1]
            second_half = nodes[N//2:]
        else:
            first_half = nodes[1:N//2+1][::-1]
            second_half = nodes[N//2+1:]
        
        curr = head
        cnt = 1
        while cnt < N:
            if cnt & 1:
                curr.next = second_half.pop()
            else:
                curr.next = first_half.pop()
            curr = curr.next
            cnt += 1
        
        curr.next = None
        return head