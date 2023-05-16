# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        og = head
        nodes = []
        
        while head:
            nodes.append(head.val)
            head = head.next
        
        for i in range(len(nodes)):
            if i & 1:
                nodes[i], nodes[i-1] = nodes[i-1], nodes[i]
        
        print(nodes)
        
        head = og = ListNode(nodes[0])
        for node in nodes[1:]:
            head.next = ListNode(node)
            head = head.next
            
        return og
            