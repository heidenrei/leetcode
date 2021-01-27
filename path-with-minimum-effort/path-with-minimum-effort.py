class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        
        INF = float('inf')
        
        DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def is_possible(limit):
            seen = set(tuple([0, 0]))
            def go(i, j):
                if i == R - 1 and j == C - 1:
                    return True
                for di, dj in DIRS:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and tuple([ni, nj]) not in seen and abs(heights[ni][nj] - heights[i][j]) <= limit:
                        seen.add(tuple([i, j]))
                        if go(ni, nj):
                            return True
                        
            return go(0, 0)
        
        l = 0
        r = max([max(x) for x in heights])
                
        while l < r:
            m = (l+r)>>1
            if is_possible(m):
                r = m
            else:
                l = m + 1
                
        return l
