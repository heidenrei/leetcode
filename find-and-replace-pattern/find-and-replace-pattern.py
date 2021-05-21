class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def matches(x):
            d = defaultdict(int)
            curr = 0
            ans = []
            for ch in x:
                if ch not in d:
                    curr += 1
                    ans.append(str(curr))
                    d[ch] = str(curr)
                else:
                    ans.append(d[ch])
                    
            return ans
        
        pattern = matches(pattern)

        out = []
        
        for x in words:
            if matches(x) == pattern:
                out.append(x)
                
        return out