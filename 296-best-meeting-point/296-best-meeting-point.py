class Solution:
    def minTotalDistance(self, A):
        R, C = len(A), len(A[0])
        
        rowsum = []
        for i in range(R):
            rowsum.append(sum(A[i]))
        
        rowpfs = list(accumulate(rowsum))
        
        rowsum.reverse()
        
        rowpfsup = list(accumulate(rowsum))[::-1]
        # print(rowpfsup)
        # print()
        pre = []
        suf = []
        
        for i in range(R):
            curr = 0
            cnt = 0
            tmp = []
            for j in range(C):
                tmp.append(curr)
                cnt += A[i][j]
                curr += cnt
            pre.append(tmp)
            
            curr = 0
            tmp = []
            cnt = 0
            for j in range(C-1, -1, -1):
                tmp.append(curr)
                cnt += A[i][j]
                curr += cnt
            suf.append(tmp[::-1])
            
#         for x in pre:
#             print(x)
#         print()
#         for x in suf:
#             print(x)
            
        down = [[0 for x in range(C)] for y in range(R)]
        down[0] = [pre[0][j] + suf[0][j] for j in range(C)]
        up = [[0 for x in range(C)] for y in range(R)]
        up[R-1] = [pre[R-1][j] + suf[R-1][j] for j in range(C)]
        
        for j in range(C):
            for i in range(1, R):
                tmp = rowpfs[i-1] + down[i-1][j]
                tmp += pre[i][j]
                tmp += suf[i][j]
                    
                down[i][j] = tmp
        # print()
        # for x in down:
        #     print(x)
            
        for j in range(C):
            for i in range(R-2, -1, -1):
                tmp = rowpfsup[i+1] + up[i+1][j]
                tmp += pre[i][j]
                tmp += suf[i][j]
                
                up[i][j] = tmp
        
#         print()
#         for x in up:
#             print(x)
        
        best = inf
        for i in range(R):
            for j in range(C):
                tmp = up[i][j] + down[i][j] - pre[i][j] - suf[i][j]
                if tmp < best:
                    best = tmp
                    
        return best
            
            