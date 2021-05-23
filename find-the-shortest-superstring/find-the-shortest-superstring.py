class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        N = len(words)
        overlaps = [[0 for x in range(N)] for y in range(N)]
        
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                    
                x, y = words[i], words[j]
                
                for k in range(1, len(x)):
                    if y.startswith(x[k:]):
                        overlaps[i][j] = len(x) - k
                        break
        @cache          
        def go(i, bm):
            if bm == 2**N-1:
                return words[i]
            
            ans = '#'*320
            
            for j in range(N):
                if not bm & (1<<j):
                    
                    k = overlaps[i][j]
                    
                    tmp = go(j, bm | (1<<j))
                                        
                    if len(words[i] + tmp[k:]) < len(ans):
                        ans = words[i] + tmp[k:]
                        
            return ans
                        
        return min([go(i, 1 << i) for i in range(N)], key=len)