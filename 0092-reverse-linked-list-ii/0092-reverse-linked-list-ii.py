# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        nodes = []
        left -= 1
        right -= 1
        curr = head
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        
        nodes = nodes[:left] + nodes[left:right+1][::-1] + nodes[right+1:]

        nodes.reverse()
        
        
        curr = head
        while curr:
            curr.val = nodes.pop()
            curr = curr.next
            
        return head