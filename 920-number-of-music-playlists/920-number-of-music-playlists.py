class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9+7
        dp = [[0 for x in range(n+1)] for y in range(goal+1)]
        dp[0][0] = 1 # i = num songs used, j = playlist length
        for i in range(1, goal+1):
            for j in range(1, n+1):
                # add new song
                #if dp[i-1][j] == 0:
                dp[i][j] = (n-j+1)*dp[i-1][j-1]
                dp[i][j] %= MOD
                
                #else:# dp[i-1][j] > 0.. add already added song again
                dp[i][j] += dp[i-1][j]*(max(j-k, 0))
                dp[i][j] %= MOD
        
        # for x in dp:
        #     print(x)
        # print()
        return dp[-1][-1]