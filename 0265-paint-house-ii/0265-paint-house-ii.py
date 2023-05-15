class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # each house is either the cheapest or second cheapest color
        N= len(costs)
        @cache
        def go(i, j):
            if i == N:
                return 0
            ans = inf
            for nj in range(len(costs[i])):
                if nj != j:
                    tmp = go(i+1, nj) + costs[i][nj]
                    if tmp < ans:
                        ans = tmp
                        
            return ans
        
        return min(go(1, j) + costs[0][j] for j in range(len(costs[0])))