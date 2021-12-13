class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        best = 1
        curr = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
                best = max(best, curr)
            else:
                curr = 1
                
        return best