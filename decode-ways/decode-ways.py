class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        idx = 0
        
        @cache
        def go(idx):
            if idx == N:
                return 1
            total = 0
            
            if idx + 1 < N and s[idx] in '2' and s[idx+1] not in '789':
                total += go(idx+2)
                
            if s[idx] != '0':
                total += go(idx+1)
                
            if idx + 1 < N and s[idx] == '1':
                total += go(idx+2)
            
            return total
        
        return go(0)