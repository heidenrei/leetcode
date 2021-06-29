class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if (not word1 and not word2) or word1 == word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        @cache
        def go(i, j):
            if i == -1 and j == -1:
                return 0
            
            if i == -1 or j == -1:
                return abs(i - j)
            
            best = math.inf
            if word1[i] == word2[j]:
                best = go(i-1, j-1)
                
            else:
                if i - 1 >= -1:
                    best = 1 + go(i-1, j)
                    if j - 1 >= -1:
                        best = min(best, 1 + go(i-1, j-1))
                if j -1 >= -1:
                    best = min(best, 1 + go(i, j-1))
                
                
            return best
        
        return go(len(word1)-1, len(word2)-1)
                