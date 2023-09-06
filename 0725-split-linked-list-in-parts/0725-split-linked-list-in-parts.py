# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        og = head
        while head:
            n += 1
            head = head.next
        
        q, r = divmod(n, k)
        head = og
        cnt = 0
        ans = []
        while head:
            cnt += 1
            if cnt == 1:
                #ans.append()
                ans.append(head)
            #ans.append(head)
            if cnt == q:
                if r:
                    r -= 1
                    head = head.next
                else:
                    cnt = 0
                    prev = head
                    head = head.next
                    prev.next = None
            elif cnt == q+1:
                prev = head
                head = head.next
                prev.next = None
                cnt = 0
            else:
                head = head.next
                
        while len(ans) < k:
            ans.append(None)
            #ans.append([None])
        #print(ans)
        return ans