class Solution:
    def isPathCrossing(self, path: str) -> bool:
        N = len(path)
        
        seen = set([tuple([0, 0])])
        
        dirs = {'N': [-1, 0], 'E': [0, 1], 'S': [1, 0], 'W': [0, -1]}
        
        i = j = 0
        
        for idx in range(N):
            di, dj = dirs[path[idx]]
            i, j = i + di, j + dj
            if tuple([i, j]) not in seen:
                seen.add(tuple([i, j]))
            else:
                return True
            
            
                
