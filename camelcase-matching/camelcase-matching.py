class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        
        def get_pattern(s):
            N = len(s)
            ans = ''
            i = 0
            pi = 0
            while i < N and pi < len(pattern):
                if s[i] == pattern[pi] or s[i].isupper():
                    ans += s[i]
                    i += 1
                    pi += 1
                else:
                    i += 1
            
            while i < N:
                if s[i].isupper():
                    ans += s[i]
                i += 1
            
            return ans
        
        out = []
        
        for s in queries:
            #print(get_pattern(s))
            out.append(get_pattern(s) == pattern)

            
        return out
    