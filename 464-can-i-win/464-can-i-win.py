class Solution:
    def canIWin(self, m: int, k: int) -> bool:
        @cache
        def go(bm):
            pop_count = 0
            s = 0
            for x in range(1, m+1):
                if bm & (1<<x):
                    s += x
                    pop_count += 1
            
            ans = []
            for x in range(1, m+1):
                if not bm & (1<<x):
                    if s + x >= k:
                        return True
                    if not go(bm | (1<<x)):#ans.append()):
                        return True
            return False    

        if m >= k:
            return True
        if (m*(m+1))//2 < k:
            return False
        
        return go(0)