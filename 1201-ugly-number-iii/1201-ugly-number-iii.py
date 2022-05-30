class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        def ugly_cnt(nn):
            ans = nn//a + nn//b + nn/c
            ans -= nn//lcm(a, b) + nn//lcm(a, c) + nn//lcm(b, c)
            ans += nn//lcm(a, b, c)
            return ans
        #a * bc // math.gcd(a, bc)
        
        l = 0
        r = 2**31-1
        
        while l <= r:
            m = (l+r)>>1
            if ugly_cnt(m) < n:
                l = m + 1
            else:
                r = m - 1
                
        return r + 1