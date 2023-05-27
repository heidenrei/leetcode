class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9+7
        @cache
        def go(i, prev, remk):
            if remk < 0:
                return 0
            if i == n:
                if not remk:
                    return 1
                else:
                    return 0
            ans = 0
            for x in range(1, m+1):
                if x > prev:
                    ans += go(i+1, x, remk-1)
                    ans %= MOD
                else:
                    ans += go(i+1, prev, remk)
                    ans %= MOD
            return ans
            
    
        return go(0, -1, k)
        # ans = 0
        # for x in range(1, m+1):
        #     ans += go(0, x, k)
        #     ans %= MOD
        # return ans