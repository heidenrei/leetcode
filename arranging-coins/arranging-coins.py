class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
            
        l = 0
        h = n
        
        while l <= h:
            m = (l + ((h-l) // 2))
            total = (m*(m+1))//2
            
            if total == n:
                return m
            
            if total < n:
                l = m + 1
            else:
                h = m - 1
            
        return h