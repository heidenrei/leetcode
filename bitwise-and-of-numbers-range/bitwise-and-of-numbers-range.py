class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        cnt = 0
        while m != n:
            n //= 2
            m //= 2
            cnt += 1
            
        return m << cnt
            