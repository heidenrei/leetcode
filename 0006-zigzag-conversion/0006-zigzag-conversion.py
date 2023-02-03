class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        out = [['!']*len(s) for x in range(numRows)]
        
        DIRS = deque([[1, 0], [-1, 1]])
        i = j = 0
        
        for c in s:
            out[i][j] = c
            di, dj = DIRS[0]
            ni, nj = i + di, j + dj
            if ni == numRows or ni == -1:
                DIRS.rotate()
                di, dj = DIRS[0]
                ni, nj = i + di, j + dj
                i, j = ni, nj
                
            else:
                i, j = ni, nj
        
        ans = ''
        
        for i in range(numRows):
            for j in range(len(s)):
                if out[i][j] != '!':
                    ans += out[i][j]
                    
        return ans