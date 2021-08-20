class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def go(i, j):
            for x in range(9):
                seen = set()
                for y in range(9):
                    if board[x][y] != '.':
                        if board[x][y] not in seen:
                            seen.add(board[x][y])
                        else:
                            return False
            
            for y in range(9):
                seen = set()
                for x in range(9):
                    if board[x][y] != '.':
                        if board[x][y] not in seen:
                            seen.add(board[x][y])
                        else:
                            return False
                        
            for x in range(0, 9, 3):
                for y in range(0, 9, 3):
                    seen = set()
                    for dx in range(3):
                        for dy in range(3):
                            if board[x + dx][y + dy] != '.':
                                if board[x + dx][y + dy] not in seen:
                                    seen.add(board[x + dx][y + dy])
                                else:
                                    return False
                                
            return True
        
        return go(0, 0)