class Solution:
    def ways(self, A, K) -> int:
        MOD = 10**9+7
        R, C = len(A), len(A[0])
        
        pfs = [[0 for x in range(C+1)] for y in range(R+1)]
        for i in range(R - 1, -1, -1):
            for j in range(C - 1, -1, -1):
                pfs[i][j] = pfs[i][j + 1] + pfs[i + 1][j] - pfs[i + 1][j + 1] + (A[i][j] == 'A')

        for x in pfs:
            print(x)
                
        @cache
        def go(k, i, j):
            if pfs[i][j] == 0:
                return 0
            if k == 0:
                return 1
            
            ans = 0
            # cut horizontally
            for ni in range(i + 1, R):
                if pfs[i][j] - pfs[ni][j] > 0:
                    ans += go(k - 1, ni, j)
                    ans %= MOD
            # cut vertically                    
            for nj in range(j + 1, C):
                if pfs[i][j] - pfs[i][nj] > 0:
                    ans += go(k - 1, i, nj)
                    ans %= MOD
            return ans

        return go(K - 1, 0, 0)