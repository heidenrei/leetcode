class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R, C = len(board), len(board[0])
        
        DIRS = [-1,-1, 0, 0,1, 1]
        DIRS = list(set([x for x in permutations(DIRS, 2) if x != (0, 0)]))
        
        def go(i, j):
            cnt = 0
            if board[i][j] == 'M':
                board[i][j] = 'X'
                return
            for di, dj in DIRS:
                ni, nj = di + i, dj + j

                if 0 <= ni < R and 0 <= nj < C:
                    if board[ni][nj] == 'M':
                        cnt += 1
                        
            if not cnt:
                board[i][j] = 'B'
                for di, dj in DIRS:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < R and 0 <= nj < C and board[ni][nj] == 'E':
                        go(ni, nj)
            else:
                board[i][j] = str(cnt)
                
        go(click[0], click[1])
        
        return board
