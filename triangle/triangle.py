class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        R, C = len(triangle), len(triangle[-1])
        INF = float('inf')
        dp = [[INF for x in range(C)] for y in range(R)]
        dp[0][0] = triangle[0][0]
        DIRS = [[1, 1], [1, 0]]
        
        level = 0
        while level < R-1:
            for j in range(1, level+2):
                dp[level+1][j] = min(dp[level][j], dp[level][j-1]) + triangle[level+1][j]
            dp[level+1][0] = dp[level][0] + triangle[level+1][0]
            level += 1
            
                
                
        return min(dp[-1])