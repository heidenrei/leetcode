class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = Counter(arr)
        if c[0] & 1:
            return False
        
        pos = [x for x in arr if x > 0]
        c = Counter(pos)
        pos.sort()
        sa = set(pos)
        for x in pos:
            if c[x] and x*2 in sa and c[x*2] > 0:
                c[x*2] -= 1
                c[x] -= 1
                
            elif c[x] > 0:
                return False
            
        neg = [abs(x) for x in arr if x < 0]
        c = Counter(neg)
        neg.sort()
        sa = set(neg)
        for x in neg:
            if c[x] and x*2 in sa and c[x*2] > 0:
                c[x*2] -= 1
                c[x] -= 1

                
            elif c[x] > 0:
                return False
            
        return True