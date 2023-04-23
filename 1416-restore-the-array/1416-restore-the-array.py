class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        s = [int(x) for x in s]
        N, M = len(s), len(str(k))
        MOD = 10**9+7
        # need 2 cases... equal to k and less than k..
        # equal...
        # less than k just count digits
        @cache
        def go(i):
            if i == N:
                return 1
            ans = 0
            curr = 0
            for j in range(i+1, min(N+1, i+M+1)):
                curr =  curr*10 + s[j-1]
                if int(curr) > k:
                    break
                if j == N or s[j]:
                    #print(i, j)
                    ans += go(j)
                    ans %= MOD
            return ans
        return go(0)