class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        
        DIRS = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        
        #@cache
        def go(i, j):
            seen = set()
            
            level = 0
            q = [[i, j]]
            
            while q:
                tmp = []
                while q:
                    i, j = q.pop()
                    if mat[i][j] == 0:
                        return level
                    for di, dj in DIRS:
                        ni, nj = di + i, dj + j
                        if 0 <= ni < R and 0 <= nj < C and tuple([ni, nj]) not in seen:
                            seen.add(tuple([ni, nj]))
                            tmp.append([ni, nj])
                q.extend(tmp)
                level += 1
            
            return math.inf
                    
        ans = []            
        
        for i in range(R):
            tmp = []
            for j in range(C):
                tmp.append(go(i, j))
            ans.append(tmp)
            
        return ans