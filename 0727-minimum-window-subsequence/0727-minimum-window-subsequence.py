class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        N, M = len(s1), len(s2)
        @cache
        def go(i, j):
            if j == M:
                return i
            if i == N:
                return inf
            if s1[i] == s2[j]:
                return go(i+1, j+1)
            else:
                return go(i+1, j)
            
        best = inf
        besti = None
        for i in range(N-M+1):
            ti = go(i,0)
            tmp = ti - i
            if tmp < best:
                best = tmp
                besti = i
        
        if best == inf:
            return ''
        
        ans = s1[besti:besti+best]
        return ans