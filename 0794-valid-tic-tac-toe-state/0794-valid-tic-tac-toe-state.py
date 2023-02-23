class Solution:
    def validTicTacToe(self, A: List[str]) -> bool:
        c = Counter()
        for i in range(3):
            for j in range(3):
                c[A[i][j]] += 1
                
        for i in range(3):
            A[i] = [x for x in A[i]]
        
        if c['X'] - c['O'] > 1 or c['O'] > c['X']:
            return False
        
        x_wins = False
        o_wins = False
        for i in range(3):
            if A[i][0] == 'X' and len(set(A[i])) == 1:
                if x_wins or o_wins:
                    return False
                x_wins = True
            if A[i][0] == 'O' and len(set(A[i])) == 1:
                if x_wins or o_wins:
                    return False
                o_wins = True
        
        if x_wins and c['O'] == c['X']:
            return False
        if o_wins and c['X'] > c['O']:
            return False
        
        x_wins = False
        o_wins = False
        for j in range(3):
            if A[0][j] == 'O' and A[1][j] == 'O' and A[2][j] == 'O':
                if x_wins or o_wins:
                    return False
                o_wins = True
            if A[0][j] == 'X' and A[1][j] == 'X' and A[2][j] == 'X':
                if x_wins or o_wins:
                    return False
                x_wins = True
        
        if x_wins and c['O'] == c['X']:
            return False
        if o_wins and c['O'] < c['X']:
            return False
        
        if A[1][1] == 'X':
            if (A[0][0] == 'X' and A[2][2] == 'X') or (A[2][0] == 'X' and A[0][2] == 'X'):
                return c['X'] > c['O']
        if A[1][1] == 'O':
            if (A[0][0] == 'O' and A[2][2] == 'O') or (A[2][0] == 'O' and A[0][2] == 'O'):
                return c['X'] == c['O']
        return True