class Solution:
    def hasValidPath(self, A):
        R, C = len(A), len(A[0])
        d = {('RIGHT', 1): ('RIGHT', (0,1)),
             ('LEFT', 1): ('LEFT', (0,-1)),
             ('DOWN', 2): ('DOWN', (1, 0)),
             ('UP', 2): ('UP', (-1, 0)),
             ('RIGHT', 3): ('DOWN', (1, 0)),
             ('UP', 3): ('LEFT', (0,-1)),
             ('UP', 4): ('RIGHT', (0,1)),
             ('LEFT', 4): ('DOWN', (1, 0)),
             ('RIGHT', 5): ('UP', (-1, 0)),
             ('DOWN', 5): ('LEFT', (0,-1)),
             ('DOWN', 6): ('RIGHT', (0,1)),
             ('LEFT', 6): ('UP', (-1, 0))
            }
        seen = set()
        def go(i, j, prev):
            if ((i, j)) not in seen:
                seen.add((i, j))
            else:
                return False
            #print(i, j, prev)
            if i == R - 1 and j == C - 1:
                return (prev, A[i][j]) in d
            # print((prev, A[i][j]))
            # print()
            if not (0 <= i < R and 0 <= j < C) or ((prev, A[i][j]) not in d):
                # print(i, j, prev, A[i][j])
                # print((prev, A[i][j]) in d)
                # print('111')
                return False
            nxt, (di, dj) = d[(prev, A[i][j])]
            return go(i + di, j + dj, nxt)
        
        if A[0][0] == 1:
            return go(0, 0, 'RIGHT')
        if A[0][0] == 2:
            return go(0, 0, 'DOWN')
        if A[0][0] == 3:
            return go(0, 0, 'RIGHT')
        if A[0][0] == 4:
            if go(0, 0, 'LEFT'):
                return True
            seen = set()
            return go(0, 0, 'UP')
        if A[0][0] == 5:
            return go(0, 0, 'RIGHT')
        if A[0][0] == 6:
            return go(0, 0, 'DOWN')