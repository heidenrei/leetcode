class Solution:
    def maxDistance(self, A):
        R, C = len(A), len(A)
        
        best = -1
        
        dp = [[A[y][x] for x in range(C)] for y in range(R)]
        
        for i in range(R):
            for j in range(C):
                dp[i][j] = 0
                if A[i][j] == 0:
                    dp[i][j] = math.inf
                
        for i in range(R):
            for j in range(C):
                if A[i][j] == 1:
                    dp[i][j] = 0
        
        curr = math.inf
        for j in range(C):
            if dp[0][j] == math.inf:
                curr += 1
                dp[0][j] = curr
            else:
                curr = 0
                
        curr = math.inf   
        for j in range(C)[::-1]:
            if dp[0][j] != 0:
                curr += 1
                dp[0][j] = min(dp[0][j], curr)
            else:
                curr = 0
                
        def set_row(row_idx):
            curr = math.inf
            for j in range(C):
                if dp[row_idx][j] != 0:
                    curr += 1
                    dp[row_idx][j] = min(curr, dp[i-1][j] + 1)
                else:
                    curr = 0
            
            curr = math.inf 
            for j in range(C)[::-1]:
                if dp[row_idx][j] != 0:
                    curr += 1
                    dp[row_idx][j] = min([dp[row_idx-1][j]+1, dp[row_idx][j], curr])
                else:
                    curr = 0
                    
                
        def set_row_from_bottom(row_idx):
            curr = math.inf
            for j in range(C):
                if dp[row_idx][j] != 0:
                    curr += 1
                    dp[row_idx][j] = min([curr, dp[row_idx+1][j] + 1, dp[row_idx][j]])
                else:
                    curr = 0
            
            curr = math.inf 
            for j in range(C)[::-1]:
                if dp[row_idx][j] != 0:
                    curr += 1
                    dp[row_idx][j] = min([dp[row_idx+1][j]+1, dp[row_idx][j], curr])
                else:
                    curr = 0
            
        
        for i in range(1, R):
            set_row(i)
            
        for i in range(R-1)[::-1]:
            set_row_from_bottom(i)
        
        ans = max(max(x) for x in dp)
        
        print(dp)
        
        return ans if ans not in [0, math.inf] else -1
                