class Solution:
    def minExtraChar(self, s: str, d):
        N = len(s)
        @cache
        def go(i):
            if i == N:
                return 0
            ans = go(i+1) + 1
            for x in d:
                if i + len(x) <= N and s[i:i+len(x)] == x:
                    tmp = go(i+len(x))
                    if tmp < ans:
                        ans = tmp
            return ans
        return go(0)