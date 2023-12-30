class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        @cache
        def go(i, j):
            if i == j or i > j:
                return 0
            ans = inf
            ans = min(ans, go(i+1, j)+1)
            ans = min(ans, go(i, j-1)+1)
            if s[i] == s[j]:
                ans = min(ans, go(i+1, j-1))
            return ans
        return go(0, n-1) <= k
                        