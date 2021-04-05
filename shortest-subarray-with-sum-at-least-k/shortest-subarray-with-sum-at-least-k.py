class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        pfs = list(accumulate(A, initial=0))
        N = len(pfs)

        d = deque()
        ans = math.inf
        
        # increasing deque
        for i in range(N):
            while (d and d[-1][1] >= pfs[i]):
                d.pop()
            while d and pfs[i] - d[0][1] >= K:
                if i - d[0][0] < ans:
                    ans = i - d[0][0]
                d.popleft()
                
            d.append([i, pfs[i]])
        
        
        return ans if ans != math.inf else -1