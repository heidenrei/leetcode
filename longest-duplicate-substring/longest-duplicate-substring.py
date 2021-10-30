class Solution:
    def longestDupSubstring(self, s: str) -> str:
        N = len(s)
        def is_good(x):
            ss = set()
            for i in range(N-x+1):
                if s[i:i+x] in ss:
                    return True
                ss.add(s[i:i+x])
            return False
        
        l = 1
        r = N-1
        
        # for x in range(1, 5):
        #     print(x, is_good(x))
        
        while l < r:
            m = l + r >> 1
            if is_good(m):
                l = m + 1
            else:
                r = m
        
        
        if not is_good(l):
            x = l - 1
        else:
            x = l
        if not is_good(x):
            return ''
        ss = set()
        for i in range(N-x+1):
            if s[i:i+x] in ss:
                return s[i:i+x]
            ss.add(s[i:i+x])
            
            