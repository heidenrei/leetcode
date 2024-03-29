class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        Ns, Np = len(s), len(p)
        
        @cache
        def go(i, j):
            if i < 0 and j < 0:
                return True
            
            elif (i < 0 and p[j] != '*') or j < 0:
                return False
            
            elif s[i] == p[j] or p[j] == '.':
                return go(i-1, j-1)
            
            elif p[j] == '*':
                if i >= 0 and (p[j-1] == s[i] or p[j-1] == '.'):
                    return go(i, j-1) or go(i-1, j) or go(i, j-2)
                
                else:
                    return go(i, j-2)
            
            return False
        
        return go(Ns-1, Np-1)