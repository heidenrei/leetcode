# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        A = []
        curr = head
        while curr:
            A.append(curr)
            curr = curr.next
        
        N = len(A)
        
        for i in range(0, N, k):
            if i+k <= N:
                A[i:i+k] = A[i:i+k][::-1]
            
        for idx, node in enumerate(A[:-1]):
            node.next = A[idx+1]
            
        A[-1].next = None
        
        return A[0]