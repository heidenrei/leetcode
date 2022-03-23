from sortedcontainers import SortedList

class Solution:
    def trapRainWater(self, A: List[List[int]]) -> int:

        R, C = len(A), len(A[0])
        DIRS = [[1,0], [0,1], [0,-1],[-1,0]]
        
        walls = set()
        seen = set()
        for i in range(R):
            walls.add((i, 0, A[i][0]))
            seen.add((i, 0))
            walls.add((i, C-1, A[i][-1]))
            seen.add((i, C-1))
        for j in range(C):
            walls.add((0, j, A[0][j]))
            seen.add((0, j))
            walls.add((R-1, j, A[R-1][j]))
            seen.add((R-1, j))
            
        pq = SortedList(walls, key=lambda x: x[2])
        level = 0
        ans = 0
        while pq:
            i, j, h = pq.pop(0)
            level = max(h, level)
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in seen:
                    if level > A[ni][nj]:
                        ans += level - A[ni][nj]
                    pq.add((ni, nj, A[ni][nj]))
                    seen.add((ni, nj))
                    
        return ans