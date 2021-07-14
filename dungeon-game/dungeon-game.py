class Solution:
    def calculateMinimumHP(self, A):
        #bf
        R, C = len(A), len(A[0])
        
        
        DIRS = [[0,1], [1,0]]
        
        
        def is_good(x):
            q = [[0, 0]]

            dp = [[-math.inf]*C for y in range(R)]
            dp[0][0] = x + A[0][0]
            if dp[0][0] < 1:
                return False
            while q:
                tmp = []
                while q:
                    i, j = q.pop()
                    if i == R - 1 and j == C - 1 and dp[i][j] > 0:
                        return True
                    for di, dj in DIRS:
                        ni, nj = di + i, dj + j
                        if 0 <= ni < R and 0 <= nj < C and dp[i][j] + A[ni][nj] > 0 and dp[i][j] + A[ni][nj] > dp[ni][nj]:
                            dp[ni][nj] = dp[i][j] + A[ni][nj]
                            tmp.append([ni, nj])
                            
                q.extend(tmp)
            
            return False
                            
        l = 1
        r = R*C*1000+1
        
        while l < r:
            m = l + r >> 1
            if is_good(m):
                r = m
            else:
                l = m + 1
        return l