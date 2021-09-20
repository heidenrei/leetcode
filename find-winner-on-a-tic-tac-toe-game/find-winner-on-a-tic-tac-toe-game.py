class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        A = [[0]*3 for _ in range(3)]
        
        def outcome():
            winner = None
            for i in range(3):
                if 0 not in A[i] and len(set(A[i])) == 1:
                    winner = A[i][0]
                    
            for j in range(3):
                tmp = []
                for i in range(3):
                    tmp.append(A[i][j])
                
                if 0 not in tmp and len(set(tmp)) == 1:
                    winner = tmp[0]
                    
            i, j = 0, 0
            tmp = []
            for _ in range(3):
                tmp.append(A[i][j])
                i += 1
                j += 1


            if 0 not in tmp and len(set(tmp)) == 1:
                winner = tmp[0]

            i, j = 2, 0
            tmp = []
            for _ in range(3):
                tmp.append(A[i][j])
                i -= 1
                j += 1

            if 0 not in tmp and len(set(tmp)) == 1:
                winner = tmp[0]

            if not winner:
                return None
            if winner == 'X':
                return 'A'
            if winner == 'O':
                return 'B'
                
                
        for idx, [x, y] in enumerate(moves):
            if idx & 1:
                A[x][y] = 'O'
            else:
                A[x][y] = 'X'
            
            tmp = outcome()
            if tmp:
                return tmp
            
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'