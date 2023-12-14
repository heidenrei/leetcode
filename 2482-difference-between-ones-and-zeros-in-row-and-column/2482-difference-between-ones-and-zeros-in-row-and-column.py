class Solution:
    def onesMinusZeros(self, A):
        R, C = len(A), len(A[0])
        diff = [[0 for x in range(C)] for y in range(R)]
        rowd, cold = [0]*R, [0]*C
        for i in range(R):
            for j in range(C):
                rowd[i] += A[i][j]
                cold[j] += A[i][j]
        for i in range(R):
            for j in range(C):
                diff[i][j] = rowd[i] + cold[j] - (R - rowd[i]) - (C - cold[j])
        
        return diff