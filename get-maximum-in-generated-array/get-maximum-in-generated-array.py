class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        A = [0, 1] + [0]*(n-1)
        for i in range(1, n+1//2):
            if 2 <= 2*i <= n:
                A[2*i] = A[i]
            if 2 <= 2*i + 1 <= n:
                A[2*i + 1] = A[i] + A[i+1]
                
        return max(A)
