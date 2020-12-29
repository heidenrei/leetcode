class Solution:
    def numberOfSteps (self, n: int) -> int:
        if n == 0:
            return 0
        cnt = 0
        def go(n):
            nonlocal cnt
            if n == 1:
                cnt += 1
                return
            
            if not (n & 1):
                cnt += 1
                go(n//2)
            else:
                cnt += 2
                go((n-1)//2)
        go(n)
        return cnt
