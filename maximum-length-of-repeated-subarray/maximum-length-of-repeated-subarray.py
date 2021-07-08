class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        NA = len(A)
        NB = len(B)
        
        dp = [[0 for x in range(NB+1)] for y in range(NA+1)]
        
        ans = 0
        
        for i in range(1, NA+1):
            for j in range(1, NB+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0
                    
                    
        return ans