class Solution:
    def strangePrinter(self, s: str) -> int:
        ns = ''
        for x in s:
            if not ns or ns[-1] != x:
                ns += x
        s = ns
        n = len(s)
        @cache
        def go(i, j):
            if i > j:
                return 0
            ans = go(i+1, j) + 1
        
            for k in range(i+1, j+1):
                if s[i] == s[k]:
                    tmp = go(i, k-1) + go(k+1, j)
                    if tmp < ans:
                        ans = tmp
            return ans
        
        return go(0, n-1)
    
# "badcbcabdbdcdb" "bacbcab" "abcacba"
# aaaaaaa
# abbbbba
# abcccba
# abcacba