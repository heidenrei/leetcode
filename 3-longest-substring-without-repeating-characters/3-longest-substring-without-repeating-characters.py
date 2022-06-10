class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        def is_good(x):
            c = Counter(s[:x])
            if len(c.keys()) == x:
                return True
            for i in range(x, N):
                c[s[i]] += 1
                c[s[i-x]] -= 1
                if c[s[i-x]] == 0:
                    del c[s[i-x]]
                if len(c.keys()) == x:
                    return True
                
            return False
        
        N = len(s)
        l, r = 0, N
        while l < r:
            m = l + (r-l+1)//2
            if is_good(m):
                l = m
            else: 
                r = m - 1
        return l