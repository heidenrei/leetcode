class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        best = s
        
        if k > 1:
            return ''.join(sorted([x for x in s]))
        
        for i in range(len(s)):
            best = min(best, s[i:] + s[:i])
            
        return best