class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for x in range(9)]
        cols = [set() for x in range(9)]
        boxes = [set() for x in range(9)]
        
        found_ans = False
                            
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3)*3 + j//3].add(board[i][j])
                    
        def go(i, j):
            nonlocal found_ans
            if not found_ans:
                if i == 9:
                    found_ans = True
                    return
                ni, nj = i + (j+1) // 9, (j + 1) % 9
                
                if board[i][j] != '.':
                    go(ni, nj)
                else:
                    for x in range(1, 10):
                        if str(x) not in rows[i] and str(x) not in cols[j] and str(x) not in boxes[(i//3)*3 + j//3]:
                            rows[i].add(str(x))
                            cols[j].add(str(x))
                            boxes[(i//3)*3 + j//3].add(str(x))
                            board[i][j] = str(x)
                            go(ni, nj)
                            if not found_ans:
                                rows[i].remove(str(x))
                                cols[j].remove(str(x))
                                boxes[(i//3)*3 + j//3].remove(str(x))
                                board[i][j] = '.'
                                
        go(0, 0)
        
        
                            
                    
                            
            