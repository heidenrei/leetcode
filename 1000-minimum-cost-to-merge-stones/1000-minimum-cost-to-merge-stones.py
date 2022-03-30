class Solution:
    def mergeStones(self, A: List[int], k: int) -> int:
        N = len(A)
        if (N-1) % (k-1) != 0:
            return -1
        pfs = list(accumulate(A, initial=0))

        @cache
        def go(i, j):
            if j - i + 1 < k:
                return 0
            ans = inf
            for m in range(i, j, k-1):
                tmp = go(i, m) + go(m+1, j)
                if tmp < ans:
                    ans = tmp
                    
            #res = min(go(i, mid) + go(mid + 1, j) for mid in range(i, j, k - 1))
            if (j - i) % (k - 1) == 0:
                ans += pfs[j + 1] - pfs[i]
            return ans
        return go(0, N - 1)