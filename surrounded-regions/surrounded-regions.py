class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # copy array and dfs from each node on the border, marking each traversed node. Then go back to the                 original board and flip all of the non-marked Os
        
        if not board:
            return
        
        R, C = len(board), len(board[0])
        
        A = [[0 for x in range(C)] for y in range(R)]
        
        def dfs(i, j):
            A[i][j] = 1
            if i - 1 >= 0 and board[i-1][j] == 'O' and A[i-1][j] == 0:
                dfs(i-1, j)
            if i + 1 < R and board[i+1][j] == 'O' and A[i+1][j] == 0:
                dfs(i+1, j)
            if j - 1 >= 0 and board[i][j-1] == 'O' and A[i][j-1] == 0:
                dfs(i, j-1)
            if j + 1 < C and board[i][j+1] == 'O' and A[i][j+1] == 0:
                dfs(i, j+1)
                
        for i in range(R):
            for j in range(C):
                if i == 0 or i == R-1 or j == 0 or j == C -1:
                    if board[i][j] == 'O':
                        dfs(i, j)
        
        print(A)
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O' and A[i][j] == 0:
                    board[i][j] = 'X'