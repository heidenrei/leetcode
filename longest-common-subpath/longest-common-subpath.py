class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        P = 10**9+7
        MOD = int('1'*19)
        pinv = pow(P, MOD-2, MOD)
        invpwrs = [1]
        for _ in range(max(map(len, paths))):
            invpwrs.append(pinv * invpwrs[-1]%MOD)
        
        rks = []
        for p in paths:
            ha = 0
            pwr = 1
            pre = [0]
            for x in p:
                ha = (ha+x*pwr)%MOD
                pwr = (pwr*P)%MOD
                pre.append(ha)
            rks.append(pre)
            
        #print(rks)
        
        def is_good(x):
            inter = None
            for rk in rks:
                hashes = {
                    (rk[i+x] - rk[i]) * invpwrs[i] % MOD
                    for i in range(len(rk)-x)}
                
                if inter is None:
                    inter = hashes
                else:
                    inter &= hashes
                    
                if not inter:
                    return False
                
            return True
        
        l = 0
        r = len(min(paths, key=len))
        
        while l < r:
            m = l + r + 1 >> 1
            if is_good(m):
                l = m
            else:
                r = m - 1
                
                    
        return l