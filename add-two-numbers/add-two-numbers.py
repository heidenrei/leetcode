# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_nums(curr):
            num = ''
            curr = curr
            while curr.next:
                num += str(curr.val)
                curr = curr.next
                
            num += str(curr.val)
            
            print(num)
            
            num = num[::-1]
            
            return int(num)
                
        outnum = get_nums(l1) + get_nums(l2)
        
        outnum = [x for x in str(outnum)]
        
        outnum = outnum[::-1]
        
        outnum = list(map(int, outnum))
        
        head = ListNode(outnum[0])
        og_head = head
        
        for i in range(1, len(outnum)):
            head.next = ListNode(outnum[i])
            head = head.next
        
        return og_head
