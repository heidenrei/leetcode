class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [set([x for x in y]) for y in arr if len(set([x for x in y])) == len(y)]
        ans = 0
        N = len(arr)
        @cache
        def go(bm):
            nonlocal ans
            s = set()
            for i in range(N):
                if bm & (1<<i):
                    s |= arr[i]
            
            ans = max(ans, len(s))
            
            for i in range(N):
                if not bm & (1<<i) and not s & arr[i]:
                    go(bm | (1<<i))
                    
                    
        go(0)
        return ans