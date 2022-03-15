class Solution:
    def minimumMoves(self, A) -> int:
        R, C = len(A), len(A[0])
        DIRS = [[1,0], [0,1]]#, [-1,0],[0,-1]]
        for x in A:
            print(x)
            
        print()
        level = 0
        q = [[0, 0, 0]]
        seen = set()
        seen.add((0, 0, 0))
        while q:
            tmp = []
            while q:
                i, j, o = q.pop()
                if (i == R-1 and j == C-2):
                    return level
                
                if o == 1 and j + 1 < C and A[i][j+1] != 1 and A[i+1][j+1] != 1 and (i, j, 0) not in seen:
                    seen.add((i, j, 0))
                    tmp.append([i, j, 0]) #vertical
                    
                if o == 0 and i + 1 < R and A[i+1][j] != 1 and A[i+1][j+1] != 1 and (i, j, 1) not in seen:
                    seen.add((i, j, 1))
                    tmp.append([i, j, 1])

                if o == 1:
                    for di, dj in DIRS:
                        tni, tnj = di + i, dj + j
                        hni, hnj = di + i + 1, dj + j
                        if 0 <= tni < R and 0 <= tnj < C and 0 <= hni < R and 0 <= hnj < C and A[tni][tnj] != 1 and A[hni][hnj] != 1 and (tni, tnj, o) not in seen:
                            seen.add((tni, tnj, o))
                            tmp.append([tni, tnj, o])

                if o == 0:
                    for di, dj in DIRS:
                        tni, tnj = di + i, dj + j
                        hni, hnj = di + i, dj + j + 1
                        if 0 <= tni < R and 0 <= tnj < C and 0 <= hni < R and 0 <= hnj < C and A[tni][tnj] != 1 and A[hni][hnj] != 1 and (tni, tnj, o) not in seen:
                            seen.add((tni, tnj, o))
                            tmp.append([tni, tnj, o])
            print(level, tmp)
            q = tmp
            level += 1
            
        return -1