class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        N = len(pairs)
        pairs.sort(key=lambda x: (x[0], x[1]))
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)