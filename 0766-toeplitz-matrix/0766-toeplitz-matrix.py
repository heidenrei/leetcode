class Solution:
    def isToeplitzMatrix(self, A: List[List[int]]) -> bool:
        R, C = len(A), len(A[0])
        ans = True
        for i in range(R):
            base = A[i][0]
            ti, tj = i, 0
            while ti < R and tj < C:
                if A[ti][tj] != base:
                    ans = False
                ti, tj = ti + 1, tj + 1
        
        for j in range(C):
            base = A[0][j]
            ti, tj = 0, j
            while ti < R and tj < C:
                if A[ti][tj] != base:
                    ans = False
                ti, tj = ti + 1, tj + 1
        return ans