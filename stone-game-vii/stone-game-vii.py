class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        N = len(stones)
        pfs = list(accumulate(stones, initial=0))
        
        cache = [[None for x in range(N)] for y in range(N)]
        
        def score(i, j):
            return pfs[j]-pfs[i]
        
        def go(i, j):
            if i == j:
                return 0
            
            if cache[i][j]:
                return cache[i][j]
            
            left = score(i+1, j+1) - go(i+1, j)
            right = score(i, j) - go(i, j-1)
            
            
            if left > right:
                ans = left
            else:
                ans = right
                
            cache[i][j] = ans
            return ans
            
        return go(0, N-1)