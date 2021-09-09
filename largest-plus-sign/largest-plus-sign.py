class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        A = [[1]*n for _ in range(n)]
        
        for i, j in mines:
            A[i][j] = 0
            
        l = [[1]*n for _ in range(n)]
        u = [[1]*n for _ in range(n)]
        r = [[1]*n for _ in range(n)]
        d = [[1]*n for _ in range(n)]

                
        for i in range(n):
            curr = 0
            for j in range(n):
                if A[i][j] == 1:
                    curr += 1
                else:
                    curr = 0
                l[i][j] = curr
                
        for i in range(n):
            curr = 0
            for j in range(n)[::-1]:
                if A[i][j] == 1:
                    curr += 1
                else:
                    curr = 0
                r[i][j] = curr
                
        for j in range(n):
            curr = 0
            for i in range(n):
                if A[i][j] == 1:
                    curr += 1
                else:
                    curr = 0
                u[i][j] = curr
        
        for j in range(n):
            curr = 0
            for i in range(n)[::-1]:
                if A[i][j] == 1:
                    curr += 1
                else:
                    curr = 0
                d[i][j] = curr
                
        best = 0
        for i in range(n):
            for j in range(n):
                best = max(best, min([l[i][j], r[i][j], u[i][j], d[i][j]]))
                
        return best