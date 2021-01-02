class Solution:
    def freqAlphabets(self, s: str) -> str:
        N = len(s)
        
        ans = []
        d = dict()
        for i in range(1, 10):
            d[str(i)] = chr(ord('a')+i-1)
            
        for i in range(10, 27):
            d[str(i) + '#'] = chr(ord('a')+i-1)
        
        idx = 0 
        while idx < N:
            if idx < N - 2:
                if s[idx+2] == '#':
                    ans.append(d[s[idx:idx+3]])
                    idx += 3
                else:
                    ans.append(d[s[idx]])
                    idx += 1
            else:
                ans.append(d[s[idx]])
                idx += 1
                
        return ''.join(ans)
