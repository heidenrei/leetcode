class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rows = set()
        cols = set()
        
        R, C = len(board), len(board[0])
        
        
        
        cnt = 0
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'R':
                    tmpi = i
                    tmpj = j
                    while tmpj >= 0:
                        if board[tmpi][tmpj] == 'p':
                            cnt += 1
                            break
                        elif board[tmpi][tmpj] == 'B':
                            break
                        tmpj -= 1
                        
                    tmpj = j
                    while tmpj < C:
                        if board[tmpi][tmpj] == 'p':
                            cnt += 1
                            break
                        elif board[tmpi][tmpj] == 'B':
                            break
                        tmpj += 1
                        
                    tmpj = j
                    while tmpi >= 0:
                        if board[tmpi][tmpj] == 'p':
                            cnt += 1
                            break
                        elif board[tmpi][tmpj] == 'B':
                            break
                        tmpi -= 1
                        
                    tmpi = i
                    while tmpi < R:
                        if board[tmpi][tmpj] == 'p':
                            cnt += 1
                            break
                        elif board[tmpi][tmpj] == 'B':
                            break
                        tmpi += 1
                            
                    break
                    
        return cnt
                            
            
                    
                    