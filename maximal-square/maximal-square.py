class Solution(object):
    def maximalSquare(self, A):
        R, C = len(A), len(A[0])
        best = 0

        for i in range(R):
            for j in range(C):
                A[i][j] = int(A[i][j])
                if A[i][j] > best:
                    best = A[i][j]
                
        for i in range(1, R):
            for j in range(1, C):
                if A[i][j] == 1:
                    mini = min([A[i-1][j], A[i-1][j-1], A[i][j-1]])
                    A[i][j] = mini + 1
                    if A[i][j]**2 > best:
                        best = A[i][j]**2
        
        return best