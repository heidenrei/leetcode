class Solution:
    def findLonelyPixel(self, A):
        R, C = len(A), len(A[0])
        for i in range(R):
            for j in range(C):
                if A[i][j] == 'B':
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        rc = defaultdict(int)
        cc = defaultdict(int)
        for i in range(R):
            for j in range(C):
                rc[i] += A[i][j]
                cc[j] += A[i][j]
                
        ans = 0
        for i in range(R):
            for j in range(C):
                ans += A[i][j] and rc[i] == 1 and cc[j] == 1
                
        return ans