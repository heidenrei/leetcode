class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i, x in enumerate(s[::-1]):
            ans += (ord(x) - ord('A') + 1) * 26**(i)
        return ans