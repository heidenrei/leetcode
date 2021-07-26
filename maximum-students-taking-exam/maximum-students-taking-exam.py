class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        R, C = len(seats), len(seats[0])
        DIRS = [[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        #@cache
        def go(bm):
            best = 0
            for j in range(C):
                if not bm & (1<<j):
                    cnt = 0
                    i_list = []
                    for i in range(R):
                        if seats[i][j] == '.':
                            possible = True
                            for di, dj in DIRS:
                                ni, nj = di + i, dj + j
                                if 0 <= ni < R and 0 <= nj < C and seats[ni][nj] == 'x':
                                    possible = False
                                    break
                            if possible:
                                cnt += 1
                                i_list.append(i)
                                seats[i][j] = 'x'
                    
                    tmp = go(bm | (1<<j)) + cnt
                    best = max(best, tmp)
                    for k in i_list:
                        seats[k][j] = '.'
                
            return best
        
        ans = go(0)
        return ans
        