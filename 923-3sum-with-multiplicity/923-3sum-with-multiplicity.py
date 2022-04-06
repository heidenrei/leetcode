class Solution:
    def threeSumMulti(self, A: List[int], k: int) -> int:
        A.sort()
        N = len(A)
        MOD = 10**9+7
        ans = 0
        rc = Counter(A[1:])
        lc = Counter(A[:1])
        for i in range(1, N):
            rc[A[i]] -= 1
            for l in range(A[i]+1):
                ans += rc[k - l - A[i]] *lc[l]
                ans %= MOD
            lc[A[i]] += 1
                
        return ans