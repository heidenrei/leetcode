class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        s = [x for x in s]
        def is_good(m):
            c = Counter(s[:m])
            keys = list(c.keys())
            cnt = len(keys)
            if cnt <= 2:
                return True
            for i in range(m, n):
                c[s[i]] += 1
                if c[s[i]] == 1:
                    cnt += 1
                c[s[i-m]] -= 1
                if c[s[i-m]] == 0:
                    cnt -= 1
                if cnt <= 2:
                    return True
            return False
        
        l, r = 1, n
        while l < r:
            m = l + (r-l+1)//2
            if is_good(m):
                l = m
            else:
                r = m - 1
        return l
                
            