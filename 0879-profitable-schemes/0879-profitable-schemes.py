class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9+7
        N = len(group)
        @cache
        def go(i, p, rem_men):
            if i == N:
                if not p:
                    return 1
                else:
                    return 0
            ans = go(i+1, p, rem_men)
            if rem_men >= group[i]:
                np = p - profit[i]
                if np < 0:
                    np = 0
                ans += go(i+1, np, rem_men-group[i])
                ans %= MOD
            return ans % MOD
        return go(0, minProfit, n)
    