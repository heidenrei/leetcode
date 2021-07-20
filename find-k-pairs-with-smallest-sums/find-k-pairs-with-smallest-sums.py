from sortedcontainers import SortedList

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        N1 = len(nums1)
        N2 = len(nums2)
        
        q = SortedList()
        q.add([nums1[0] + nums2[0], tuple([0, 0])])
        q.add([nums1[-1] + nums2[-1], tuple([N1-1, N2-1])])
        
        seen = set()
        seen.add(tuple([0, 0]))
        seen.add(tuple([N1-1, N2-1]))
        
        ans = []
        while len(ans) < k:
            if not q:
                break
            curr, x = q.pop(0)
            ans.append(x)
            i1, i2 = x
            if i1 + 1 < N1 and tuple([i1+1, i2]) not in seen:
                seen.add(tuple([i1+1, i2]))
                q.add([nums1[i1+1] + nums2[i2], tuple([i1+1, i2])])
            if i1 - 1 >= 0 and tuple([i1-1, i2]) not in seen:
                seen.add(tuple([i1-1, i2]))
                q.add([nums1[i1-1] + nums2[i2], tuple([i1-1, i2])])
            if i2 + 1 < N2 and tuple([i1, i2+1]) not in seen:
                seen.add(tuple([i1, i2+1]))
                q.add([nums1[i1] + nums2[i2+1], tuple([i1, i2+1])])
            if i2 - 1 >= 0 and tuple([i1, i2-1]) not in seen:
                seen.add(tuple([i1, i2-1]))
                q.add([nums1[i1] + nums2[i2-1], tuple([i1, i2-1])])
                
        return [[nums1[x[0]], nums2[x[1]]] for x in ans]