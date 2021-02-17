class Solution:
    def pacificAtlantic(self, A):
        if not A:
            return []
        
        R, C = len(A), len(A[0])
        
        DIRS = [[1, 0], [0, 1], [-1, 0], [0,-1]]

        ans = []
        
        def go(i, j):
            for di, dj in DIRS:
                ni, nj = i + di, j + dj
                if 0 > ni or 0 > nj:
                    nonlocal P
                    P = True
                if ni >= R or nj >= C:
                    nonlocal At
                    At = True
                if 0 <= ni < R and 0 <= nj < C and A[i][j] >= A[ni][nj] and tuple([ni, nj]) not in seen:
                    seen.add(tuple([ni, nj]))
                    go(ni, nj)  
        
        for i in range(R):
            for j in range(C):
                seen = set()
                At = False
                P = False
                go(i, j)
                
                if At and P:
                    ans.append([i, j])
                    
        return ans