class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        N1 = len(cost)
        N2 = len(cost[0])

        @cache
        def go(i, bm):
            #print(bin(bm1), bin(bm2))
            if i == N1 and bm == 2**N2-1:
                return 0
            
            ans = inf
            if i < N1:
                for j in range(N2):
                    tmp = go(i+1, bm | (1<<j)) + cost[i][j]
                    if tmp < ans:
                        ans = tmp
                return ans
            else:
                ans = 0
                for j in range(N2):
                    if not bm & (1<<j):
                        ans += min([cost[i][j] for i in range(N1)])
                return ans
        
        return go(0, 0)