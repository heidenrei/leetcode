class Solution:
    def hitBricks(self, A, hits):
        R, C = len(A), len(A[0])
        A = [[1]*C] + A
        R += 1
        for i in range(len(hits)):
            hits[i][0] += 1
            
        DIRS = [[1,0],[0,1],[0,-1],[-1,0]]
        og = set()
        for i, j in hits:
            if A[i][j]:
                og.add((i, j))
            A[i][j] = 0
        
        p = defaultdict(int)
        s = defaultdict(lambda: 1)
        
        def ufind(x):
            if x not in p:
                p[x] = x
                s[x]
            if p[x] != x:
                p[x] = ufind(p[x])
            return p[x]
        
        def uunion(x, y):
            ux, uy = ufind(x), ufind(y)
            if ux == uy:
                return
            if s[ux] > s[uy]:
                uy, ux = ux, uy
            s[uy] += s[ux]
            p[ux] = uy
        
        for i in range(R):
            for j in range(C):
                if not A[i][j]:
                    continue
                for di, dj in DIRS:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < R and 0 <= nj < C and A[ni][nj]:
                        uunion((ni, nj), (i, j))
        
        ans = []
        for i, j in hits[::-1]:
            # for x in A:
            #     print(x)
            if (i,j) not in og:
                ans.append(0)
                continue
            else:
                A[i][j] = 1
            
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and ufind((ni, nj)) == ufind((0, 0)):
                    uunion((i, j), (ni, nj))
                
            before = s[ufind((0, 0))]
            #print(before)
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and A[ni][nj]:
                    uunion((i, j), (ni, nj))
            after = s[ufind((0, 0))]
            # print(after)
            # print()
            ans.append(after - before)
        return ans[::-1]