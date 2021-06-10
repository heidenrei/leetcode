class Solution:
    def isLongPressedName(self, n: str, t: str) -> bool:
        tidx = 0
        nidx = 0
        
        while tidx < len(t) and nidx < len(n):
            
            if t[tidx] == n[nidx]:
                if tidx == len(t) - 1 and nidx == len(n) - 1:
                    return True
                
                curr = t[tidx]
                tcnt = ncnt = 0
                
                while t[tidx] == curr and tidx + 1 < len(t):
                    tidx += 1
                    tcnt += 1
                    
                while n[nidx] == curr and nidx + 1 < len(n):
                    nidx += 1
                    ncnt += 1
                
                if tcnt < ncnt:
                    return False
                
            else:
                return False
            
        return True