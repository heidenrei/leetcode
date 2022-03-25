class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        @cache
        def go(i, ac, bc):
            if i == N and ac == N//2 and bc == N//2:
                return 0
            if i == N or ac > N//2 or bc > N//2:
                return inf
            ans = inf
            
            ans = min(ans, go(i+1, ac+1, bc) + costs[i][0])
            ans = min(ans, go(i+1, ac, bc+1) + costs[i][1])
            return ans
        
        return go(0, 0, 0)