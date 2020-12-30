class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        
        nei = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, 0], [1, 1], [1, -1]]
        
        arr = [[0 for x in range(C)] for y in range(R)]
        
        for i in range(R):
            for j in range(C):
                cnt = 0
                for di, dj in nei:
                    if 0 <= i + di < R and 0 <= j + dj < C:
                        cnt += board[i + di][j + dj]
                # 1, 2, 3
                if board[i][j] == 1:
                    if cnt == 2 or cnt == 3:
                        arr[i][j] = 1
                # 4
                else:
                    if cnt == 3:
                        arr[i][j] = 1
        
        for i in range(R):
            for j in range(C):
                board[i][j] = arr[i][j]
