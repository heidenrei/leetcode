class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        moves = 1
        dp = [0] + [1]*K
        while dp[-1] < N:
            dp[1:] = [dp[i-1] + dp[i] + 1 for i in range(1, len(dp))]
            moves += 1
        return moves
