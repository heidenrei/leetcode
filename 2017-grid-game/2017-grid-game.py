class Solution:
    def gridGame(self, A: List[List[int]]) -> int:
        N = len(A[0])
        pfs1 = [A[1][0]]
        sfs0 = [A[0][-1]]
        for x in A[1][1:]:
            pfs1.append(pfs1[-1] + x)
        
        for x in A[0][:-1][::-1]:
            sfs0.append(sfs0[-1] + x)
            
        sfs0.reverse()
        # print(sfs0)
        # print(pfs1)

        best = inf
        for i in range(N):
            p = 0
            if i > 0:
                p = pfs1[i-1]
            s = 0
            if i < N-1:
                s = sfs0[i+1]
            best = min(best, max(p, s))
            
        return best
        
        