class Solution:
    def maxVacationDays(self, flights, days):
        N = len(flights)
        K = len(days[0])
        @cache
        def go(i, j): # i is curr city, j is week
            if j == K:
                return 0
            ans = go(i, j+1) + days[i][j]
            for ni in range(K):
                if flights[i][ni]:
                    tmp = go(ni, j+1) + days[ni][j]
                    if tmp > ans:
                        ans = tmp
            return ans
        return go(0, 0)