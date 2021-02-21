class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R, C = len(isWater), len(isWater[0])
        
        ans = [['x' for x in range(C)] for y in range(R)]
        
        q = deque()

        
        for i in range(R):
            for j in range(C):
                if isWater[i][j] == 1:
                    q.append([i, j])
        
        #bfs away from water cells
        
        DIRS = [[1,0], [0,1], [-1,0], [0,-1]]
        
        level = 0
        
        while q:
            tmp = []
            seen = set()
            while q:
                i, j = q.popleft()
                if ans[i][j] == 'x':
                    ans[i][j] = level
                for di, dj in DIRS:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and ans[ni][nj] == 'x' and tuple([ni, nj]) not in seen:
                        tmp.append([ni, nj])
                        seen.add(tuple([ni, nj]))
            q.extend(tmp)
            level += 1
            
        return ans
        
        
        