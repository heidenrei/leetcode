class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        DIRS = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if [i, j] != [0, 0]:
                    DIRS.append([i, j])
        
        level = 1
        q = defaultdict(list)
        if grid[0][0] == 0:
            q[1].append([0, 0])
        grid[0][0] = 1

        while len(q[level]) > 0:
            for i, j in q[level]:
                if i == R-1 and j == C-1:
                    return level
                for di, dj in DIRS:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == 0:
                        grid[ni][nj] = 1
                        q[level+1].append([ni, nj])
            level += 1
                

        return -1