class Solution:
    def trapRainWater(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        DIRS = [[1,0], [0,1], [0,-1],[-1,0]]
            
        walls = {(A[i][0], i, 0) for i in range(R)} | {(A[i][C-1], i, C-1) for i in range(R)} | {(A[0][j], 0, j) for j in range(C)} | {(A[R-1][j], R-1, j) for j in range(C)}
        seen = {(i, 0) for i in range(R)} | {(i, C-1) for i in range(R)} | {(0, j) for j in range(C)} | {(R-1, j) for j in range(C)}
        pq = list(walls);heapify(pq)
        level = 0
        ans = 0
        
        while pq:
            h, i, j = heappop(pq)
            level = max(h, level)
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in seen:
                    #if level > A[ni][nj]:
                    ans += max(level, A[ni][nj]) - A[ni][nj]
                    heappush(pq, (A[ni][nj], ni, nj))
                    seen.add((ni, nj))
                    
        return ans