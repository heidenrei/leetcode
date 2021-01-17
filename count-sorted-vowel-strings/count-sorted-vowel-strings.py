class Solution:
    def countVowelStrings(self, n: int) -> int:
        cnt = 0
        def go(rem, lowest):
            if rem <= 0:
                nonlocal cnt
                cnt += 1
                return
            for i in range(1, lowest+1):
                go(rem-1, i)
                
        for i in range(1, 6):
            go(n-1, i)
            
        return cnt
