class Solution:
    def shortestPathAllKeys(self, A):
        A = [[x for x in y] for y in A]
        # for x in A:
        #     print(x)
        R, C = len(A), len(A[0])
        DIRS = [[1,0],[0,1],[-1,0],[0,-1]]
        k = 0
        for i in range(R):
            for j in range(C):
                if A[i][j].isalpha() and A[i][j].islower():
                    k += 1
                if A[i][j] == '@':
                    si, sj = i, j
        A[si][sj] = '.'
        dp = [[[inf for _ in range(2**6)] for x in range(C)] for y in range(R)]
        ans = 0
        q = [[si, sj, 0]]
        dp[si][sj][0] = 0
        while q:
            tmp = []
            while q:
                i, j, bm = q.pop()
                if bm.bit_count() == k:
                    return ans
                for di, dj in DIRS:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < R and 0 <= nj < C:
                        if A[ni][nj].isalpha():
                            if A[ni][nj].islower():
                                d = ord(A[ni][nj]) - ord('a')
                                nbm = bm | (1<<d)
                            else:
                                d = ord(A[ni][nj]) - ord('A')
                                if bm & (1<<d):
                                    nbm = bm
                                else:
                                    continue
                            
                        elif A[ni][nj] == '.':
                            nbm = bm
                        else:
                            continue
                        if dp[ni][nj][nbm] > dp[i][j][bm] + 1:
                            dp[ni][nj][nbm] = dp[i][j][bm] + 1
                            tmp.append([ni,nj,nbm])
            q = tmp
            ans += 1
        return -1