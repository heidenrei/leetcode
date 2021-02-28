class Solution:
    def maximalRectangle(self, A):
        if not A:
            return 0
        R, C = len(A), len(A[0])
        rows = [[0 for x in range(C)] for y in range(R)]
        cols = [[0 for x in range(C)] for y in range(R)]
        best = 0

        for i in range(R):
            tmp = 0
            for j in range(C):
                if A[i][j] == '1':
                    tmp += 1
                else:
                    tmp = 0
                rows[i][j] = tmp
        
        for j in range(C):
            tmp = 0
            for i in range(R):
                if A[i][j] == '1':
                    tmp += 1
                else:
                    tmp = 0
                cols[i][j] = tmp
        
        for i in range(R):
            for j in range(C):
                mini = rows[i][j]
                for k in range(i, i-cols[i][j], -1):
                    mini = min(mini, rows[k][j])
                    #area = mini*(cols[i][j]-k)
                    area = mini*(i-k +1)

                    best = max(best, area)
        
        return best