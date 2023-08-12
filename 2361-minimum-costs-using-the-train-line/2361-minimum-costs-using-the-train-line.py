class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], k: int) -> List[int]:
        N = len(regular)
        A = [regular, express]
        dp = [[inf for x in range(N+1)] for y in range(2)]
        dp[0][0] = 0; dp[1][0] = k
        for j in range(1, N+1):
            for i in range(2):
                dp[i][j] = dp[i][j-1] + A[i][j-1]
            if dp[0][j] + k < dp[1][j]:
                dp[1][j] = dp[0][j] + k
            if dp[0][j] > dp[1][j]:
                dp[0][j] = dp[1][j]
        
        #print(dp)
        ans = []
        for j in range(1, N+1):
            ans.append(min(dp[0][j], dp[1][j]))
        return ans