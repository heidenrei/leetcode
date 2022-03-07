class Solution:
    def maxSideLength(self, A, k):
        R, C = len(A), len(A[0])
        pfsA = []
        for x in A:
            pfsA.append(list(accumulate(x, initial=0)))
        C += 1
        def is_good(x):
            for j in range(x, C):
                tmp = 0
                for i in range(x):
                    tmp += pfsA[i][j] - pfsA[i][j-x]
                if tmp <= k:
                    return True
                for i in range(x, R):
                    tmp += pfsA[i][j] - pfsA[i][j-x]
                    tmp -= pfsA[i-x][j] - pfsA[i-x][j-x]
                    if tmp <= k:
                        return True
                    
            return False
        
        l = 0
        r = min(R, C-1)
        while l < r:
            m = l + r >> 1
            if is_good(m):
                l = m + 1
            else:
                r = m
        if is_good(l):
            return l
        return l - 1