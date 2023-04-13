class Solution:
    def smallestGoodBase(self, n: str) -> str:
        #geometric series
        # x^0+x^1+x^2...
        # num = a*((1-x**n)/(1-x))
            
            
        # for each 111, 1111111, etc bs for base?
        n = int(n)
        def is_good(base, bs, n): # -> true if >= n
            ans = 0
            for exp in range(bs):
                ans += pow(base, exp)
                if ans >= n:
                    return ans
            return 0
        
        
        #print('1111', is_good(999999999999999999, 2, n))
        
        
        bs = 61
        while bs:
            l, r = 2, n
            while l <= r:
                m = l + r >> 1
                if is_good(m, bs, n):
                    r = m - 1
                else:
                    l = m + 1
            if is_good(r+1, bs, n) == n:
                return str(r+1)
            else:
                bs -= 1
        return '0'