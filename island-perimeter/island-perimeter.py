class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    cnt = 4
                    if i - 1 >= 0:
                        if grid[i-1][j] == 1:
                            cnt -= 1
                    if j - 1 >= 0:
                        if grid[i][j-1] == 1:
                            cnt -= 1
                    if i + 1 != R:
                        if grid[i+1][j] == 1:
                            cnt -= 1
                    if j + 1 != C:
                        if grid[i][j+1] == 1:
                            cnt -= 1
                    ans += cnt
                
        return ans