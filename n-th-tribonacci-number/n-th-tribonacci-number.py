class Solution:
    def tribonacci(self, n: int) -> int:
        A = [0,1,1]
        
        if n < 3:
            return A[n]
        
        while len(A) < n+1:
            A.append(A[-1] + A[-2] + A[-3])
        
        
        return A[-1]