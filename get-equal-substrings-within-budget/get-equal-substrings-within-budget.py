class Solution:
    def equalSubstring(self, s: str, t: str, rem: int) -> int:
        N = len(s)
        
        i = 0
        j = 0
        
        best = 0
                
        def cost(j):
            return abs(ord(s[j]) - ord(t[j]))
        
        while j < N:
            while (rem >= 0 and j < N) or (j < N and cost(j) == 0):
                rem -= cost(j)
                if rem >= 0:
                    best = max(best, j - i + 1)
                j += 1
                        
            while rem <= 0 and i < j:
                rem += cost(i)
                if rem >= 0:
                    best = max(best, j - i - 1)
                i += 1
            
        return best
                
        