class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        
        ans = 0
        
        for w in words:
            tc = Counter(w)
            good = True
            for k, v in tc.items():
                if c[k] - v < 0:
                    good = False
            
            if good:
                ans += len(w)
                
        return ans