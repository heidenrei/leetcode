class Solution:
    def largestSubmatrix(self, A: List[List[int]]) -> int:
        # cnt consecutive 1s in each columns
        R, C = len(A), len(A[0])
        
        dp = [[0 for x in range(C)] for x in range(R)]
        
        for j in range(C):
            cnt = 0
            for i in range(R):
                if A[i][j] == 1:
                    cnt += 1
                else:
                    cnt = 0
                dp[i][j] = cnt
                
        best = 0
        for i in range(R):
            j = 0
            dp[i].sort()
​
            while j < C:
                if dp[i][j] != 0:
                    break
                j += 1
            
            dp[i] = dp[i][j:]
            tmp = set(dp[i])
            for num in tmp:
                best = max(best, (len(dp[i]) - dp[i].index(num))*num)
                
        return best
