class Solution:
    def numFactoredBinaryTrees(self, A):
        N = len(A)
        MOD = 10**9+7
        ans = 0
        set_A = set(A)
        
        @lru_cache(None)
        def go(root):
            cnt = 1
            for i in range(N):
                if root % A[i] == 0:
                    tmp = root // A[i]
                    
                    if tmp in set_A:
                        cnt += go(A[i]) * go(tmp)
            return cnt
        
        for root in set_A:
            ans += go(root)
            
        return ans % MOD