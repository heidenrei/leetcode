class Solution:
    def longestLine(self, A):
        R, C = len(A), len(A[0])
        def go(i, j, di, dj):
            ans = 0
            run = 0
            while 0 <= i < R and 0 <= j < C:
                if A[i][j]:
                    run += 1
                    if run > ans:
                        ans = run
                else:
                    run = 0
                i += di; j += dj
            return ans
        ans = 0
        for j in range(C):
            tmp = go(0, j, 1, 0)
            if tmp > ans:
                ans = tmp
            tmp = go(0, j, 1, 1)
            if tmp > ans:
                ans = tmp
            tmp = go(R-1, j, -1, 1)
            if tmp > ans:
                ans = tmp
        for i in range(R):
            tmp = go(i, 0, 0, 1)
            if tmp > ans:
                ans = tmp
            tmp = go(i, 0, -1, 1)
            if tmp > ans:
                ans = tmp
            tmp = go(i, 0, 1, 1)
            if tmp > ans:
                ans = tmp
        return ans