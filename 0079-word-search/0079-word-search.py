class Solution:
    def exist(self, A, word: str) -> bool:
        N = len(word)
        
        setA = set()
        for sublist in A:
            setA |= set(sublist)
        
        if not set([x for x in word]).issubset(setA):
            return False
        
        R, C = len(A), len(A[0])
        
        DIRS = [[1, 0], [0,1], [-1, 0], [0, -1]]
        
        @cache
        def go(i, j, visited):
            idx = len(visited)
            if idx == N:
                return True
            
            visited = set(visited)
            
            ans = []
            
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and word[idx] == A[ni][nj]:
                    tmp = tuple([ni, nj])
                    if tmp not in visited:
                        visited.add(tmp)
                        ans.append(go(ni, nj, tuple(visited)))
                        visited.remove(tmp)
                        
            return any(ans)
        
        for i in range(R):
            for j in range(C):
                if A[i][j] == word[0]:
                    tmp = set()
                    tmp.add(tuple([i, j]))
                    if go(i, j, tuple(tmp)):
                        return True
                    tmp.remove(tuple([i, j]))
                    
        return False
                
        