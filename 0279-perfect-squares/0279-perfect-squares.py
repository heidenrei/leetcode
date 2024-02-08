class Solution:
    def numSquares(self, n: int) -> int: 
        dp = [inf]*(n+1)
        dp[0] = 0
        squares = []
        x = 1
        while x**2 <= n:
            squares.append(x**2)
            x += 1
        
        squares.reverse()
        
        for i in range(1, n+1):
            for x in squares:
                if i - x >= 0:
                    dp[i] = min(dp[i], dp[i-x] + 1)
                
        print(dp)
                
        return dp[-1]