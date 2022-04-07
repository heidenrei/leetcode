#from sortedcontainers import SortedList

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        best = 0
        N = len(nums)
        d = defaultdict(list)
        for i in range(N):
            d[nums[i]].append(i)
        
        #sl = SortedList()
        m = inf
        for k in sorted(d.keys()):
            for j in d[k]:
                tmp = j - m
                if tmp > best:
                    best = tmp
                m = min(m, j)
                
        return best