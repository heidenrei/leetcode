class Solution:
    def stoneGameV(self, stones: List[int]) -> int:
        N = len(stones)
        # if len(set(stones)) == 1:
        #     ans = 0
        #     i = N//2
        #     while i > 0:
        #         ans += sum(stones[:i])
        #         i //= 2
        #     return ans
        pfs = list(accumulate(stones))
        @cache
        def go(i, j): #[)
            if i == j:
                return 0
            if len(set(stones[i:j+1])) == 1:
                ans = 0
                tmp = stones[i:j+1]
                i = len(tmp)//2
                while i > 0:
                    ans += sum(tmp[:i])
                    i //= 2
                return ans
            best = -inf
            for m in range(i, j):
                #lg = go(i, m)
                l = pfs[m]
                if i > 0:
                    l -= pfs[i-1]
                r = pfs[j] - pfs[m]
                #rg = go(m+1, j)
                if l < r:
                    tmp = go(i, m) + l
                elif l > r:
                    tmp = go(m+1, j) + r
                else:
                    lg = go(i, m)
                    rg = go(m+1, j)
                    if rg+r > lg+l:
                        tmp = rg+r
                    else:
                        tmp = lg+l
                if tmp > best:
                    best = tmp
                    
            return best
        
        return go(0, N-1)