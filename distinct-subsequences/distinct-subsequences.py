class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sn = len(s)
        tn = len(t)
        
        @cache
        def go(i, j):
            if j == tn:
                return 1
            if i == sn:
                return 0
            tmp = 0
            if s[i] == t[j]:
                tmp += go(i+1, j+1)
            tmp += go(i+1, j)
                    
            return tmp
                    
        return go(0, 0)