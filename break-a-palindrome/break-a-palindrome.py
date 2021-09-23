class Solution:
    def breakPalindrome(self, p: str) -> str:
        N = len(p)
        m = N // 2
        p = [x for x in p]
        made_change = False
        for i in range(N):
            if p[i] != 'a':
                if not N & 1 or i != m:
                    p[i] = 'a'
                    made_change = True
                    break
                    
        if made_change:
            return ''.join(p)
        
        for i in range(N)[::-1]:
            if p[i] == 'a':
                if not N & 1 or i != m:
                    p[i] = 'b'
                    made_change = True
                    break
                        
        if made_change:
            return ''.join(p)
        
        
        for i in range(N):
            if p[i] != 'b':
                if not N & 1 or i != m:
                    p[i] = 'b'
                    made_change = True
                    break
        
        if made_change:
            return ''.join(p)
        return ''