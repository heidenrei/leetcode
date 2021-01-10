import heapq
​
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        N = len(jobs)
        h = 12*10**7
        l = 0
        
        def is_possible(target):
            workers = [0]*k
            
            def go(idx):
                if idx == N:
                    return True
                for i in range(k):
                    if (i == 0 or workers[i] != workers[i-1]) and workers[i] + jobs[idx] <= target:
                        workers[i] += jobs[idx]
                        if go(idx+1):
                            return True
                        workers[i] -= jobs[idx]
                return False
            return go(0)
        
        m = (h+l)>>1
        while l < h:
            m = (h+l)>>1
            if is_possible(m):
                h = m
            else:
                l = m + 1
                
        return h
