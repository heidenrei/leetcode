class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        if n < 7:
            return True
        facts = []
        for p in [2, 3, 5]:
            cnt = 0
            while n % p == 0:
                n //= p
                cnt += 1
            facts.append(cnt)
        # print(2**31)
        # print(facts)
        # print(n)
        return n == 1