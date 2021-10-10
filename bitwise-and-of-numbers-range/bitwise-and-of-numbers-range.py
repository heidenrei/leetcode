class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        cnt = 0
        while m != n:
            # print(bin(m))
            # print(bin(n))
            n //= 2
            m //= 2
            cnt += 1
        
        # print(bin(m))
        # print(bin(n))
        # print()
        # print(cnt)
        return m << cnt
            