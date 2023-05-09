class Solution:
    def tourOfKnight(self, R: int, C: int, i: int, j: int) -> List[List[int]]:
        DIRS = [[1,2],[2,1],[-1,2],[1,-2], [-1,-2],[2,-1], [-2, 1],[-2,-1]]
        ans = [[-1 for x in range(C)] for y in range(R)]
        #@cache
        def go(i, j, rem):
            ans[i][j] = rem
            if rem+1 == R*C:
                return True

            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and ans[ni][nj] < 0:
                    if go(ni, nj, rem+1):
                        return True

            ans[i][j] = -1
            return False
        go(i, j, 0)
        return ans
            
                
                    
        