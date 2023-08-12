class Solution:
    def minimumSeconds(self, A: List[List[str]]) -> int:
        q = []
        R, C = len(A), len(A[0])
        DIRS = [[1,0],[0,1],[0,-1],[-1,0]]
        d = [[inf for x in range(C)] for y in range(R)]
        level = 0
        seen = set()
        for i in range(R):
            for j in range(C):
                if A[i][j] == '*':
                    q.append([i, j])
                if A[i][j] == 'S':
                    si, sj = i, j
                    seen.add((i, j))
                if A[i][j] == 'X':
                    d[i][j] = 0
                    seen.add((i, j))
        while q:
            tmp = []
            while q:
                i, j = q.pop()
                d[i][j] = level
                for di, dj in DIRS:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in seen and A[ni][nj] != '*' and A[ni][nj] != 'D' and A[ni][nj] != 'X':
                        tmp.append([ni, nj])
                        seen.add((ni, nj))
            level += 1
            q = tmp
            
        
        # for x in d:
        #     print(x)
            
        q = [[si, sj]]
        seen = set((si, sj))
        level = 0
        while q:
            tmp = []
            while q:
                i, j = q.pop()
                #print(i, j)
                if A[i][j] == 'D':
                    return level
                
                for di, dj in DIRS:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in seen and d[ni][nj] > level+1:
                        seen.add((ni, nj))
                        tmp.append([ni, nj])
            level += 1
            q = tmp
        
        return -1