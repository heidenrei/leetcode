class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ss = set(s)
        c = Counter(s)
        best = 0
        for ch in ss:
            if c[ch] < k:
                return max(self.longestSubstring(x, k) for x in s.split(ch))
                
        return len(s)