class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        @cache
        def go(i, prev):
            if i == N:
                return 0
            ans = inf
            for j in range(3):
                if j != prev:
                    tmp = go(i+1, j) + costs[i][j]
                    if tmp < ans:
                        ans = tmp
            return ans
        return go(0, 3)