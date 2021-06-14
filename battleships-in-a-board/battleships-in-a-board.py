class Solution:
    def countBattleships(self, A):
        R, C = len(A), len(A[0])
        DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ans = 0
        
        def dfs(i, j):
            A[i][j] = '.'
            for di, dj in DIRS:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C and A[ni][nj] == 'X':
                    dfs(ni, nj)
                    
        for i in range(R):
            for j in range(C):
                if A[i][j] == 'X':
                    ans += 1
                    dfs(i, j)
                    
        return ans