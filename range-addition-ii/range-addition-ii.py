class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        mx, my = m, n
        
        for x, y in ops:
            mx = min(mx, x)
            my = min(my, y)
            
        return mx*my
            
        