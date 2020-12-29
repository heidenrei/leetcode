class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        
        ans = [-1 for x in range(C)]
        def go(i, j, ball):
            if i == R-1:
                if grid[i][j] == -1 and j >= 1 and grid[i][j-1] == -1:
                    ans[ball] = j-1
                    return
                elif grid[i][j] == 1 and j < C-1 and grid[i][j+1] == 1:
                    ans[ball] = j+1
                    return
                else:
                    return
​
            if grid[i][j] == -1 and j >= 1 and grid[i][j-1] == -1:
                go(i+1, j-1, ball)
            elif grid[i][j] == 1 and j < C-1 and grid[i][j+1] == 1:
                go(i+1, j+1, ball)
            else:
                return
        for i in range(C):
            go(0, i, i)
        
        return ans
