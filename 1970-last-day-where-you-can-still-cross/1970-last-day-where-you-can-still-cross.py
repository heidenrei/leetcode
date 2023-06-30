class Solution:
    def latestDayToCross(self, R: int, C: int, cells: List[List[int]]) -> int:
        
        DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def is_good(day):
            A = [[0]*C for _ in range(R)]
            
            for x, y in cells[:day]:
                A[x-1][y-1] = 1
                
            q = deque()
            seen = set()
            for j in range(C):
                if A[0][j] == 0:
                    q.append([0, j])
                    seen.add(tuple([0, j]))
            
            level = 0
            while q:
                tmp = []
                while q:
                    i, j = q.popleft()
                    for di, dj in DIRS:
                        ni, nj = di + i, dj + j
                        if 0 <= ni < R and 0 <= nj < C and A[ni][nj] == 0 and tuple([ni, nj]) not in seen:
                            if ni == R - 1:
                                return True
                            tmp.append([ni, nj])
                            seen.add(tuple([ni, nj]))
                            
                q = deque(tmp)
                #A[cells[day+level][0]-1][cells[day+level][1]-1] = 1
                level += 1
                
            return False

        
        l = 0
        r = R*C

        while l < r:
            m = l + r >> 1
            if is_good(m):
                l = m + 1
            else:
                r = m
                
        return l - 1