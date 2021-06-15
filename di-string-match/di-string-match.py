class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        N = len(s)
        d = deque([str(x) for x in range(N+1)])
        ans = []
        
        for ch in s:
            if ch == 'I':
                ans += [d.popleft()]
            else:
                ans += [d.pop()]
        
        return ans + [d[0]]