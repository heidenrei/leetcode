class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        N = len(piles)
        pfs = []
        for x in piles:
            pfs.append(list(accumulate(x)))
            
        @cache
        def go(i, rem):
            if i == N:
                return 0
            ans = go(i+1, rem)
            for j in range(min(len(piles[i]), rem)):
                #print(piles[i], j)
                tmp = go(i+1, rem-j-1) + pfs[i][j]
                if tmp > ans:
                    ans = tmp
                    
            return ans
        
        return go(0, k)