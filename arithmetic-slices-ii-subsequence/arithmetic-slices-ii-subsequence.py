class Solution:
    def numberOfArithmeticSlices(self, A):
        N = len(A)
        dp = [defaultdict(int) for _ in range(N)]
        
        ans = 0
        
        for i in range(N):
            for j in range(i):
                diff = A[i] - A[j]
                ans += dp[j][diff]
                dp[i][diff] += dp[j][diff] + 1
                
        return ans