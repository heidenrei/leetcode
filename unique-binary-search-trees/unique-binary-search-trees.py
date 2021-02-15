class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]*(n+1)

        # i is the number of nodes (and idx in dp array)
        for i in range(2, n+1):
            total = 0
            # x is the root of bst
            for x in range(1, i+1):
                left = x - 1
                right = i - x
                total += dp[left] * dp[right]
            dp[i] = total
        
        return dp[n]
                    
                    