class Solution:
    def diagonalSum(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        i = j = 0
        ans = 0
        while i < R and j < C:
            ans += A[i][j]
            #print(A[i][j])
            i += 1
            j += 1
        i = 0
        j = C-1
        while i < R and j >= 0:
            ans += A[i][j]
            #print(A[i][j])
            i += 1
            j -= 1
        
        if R & 1:
            ans -= A[R//2][C//2]
        
        return ans