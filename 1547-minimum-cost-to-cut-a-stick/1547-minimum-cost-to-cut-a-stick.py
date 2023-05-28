class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0);cuts.append(n)
        cuts.sort()
        @cache
        def go(i, j):
            if i + 1 == j:
                return 0
            ans = inf
            for k in range(i+1, j):
                tmp = go(i, k) + go(k, j) + cuts[j] - cuts[i]
                if tmp < ans:
                    ans = tmp
            return ans
        return go(0, len(cuts)-1)