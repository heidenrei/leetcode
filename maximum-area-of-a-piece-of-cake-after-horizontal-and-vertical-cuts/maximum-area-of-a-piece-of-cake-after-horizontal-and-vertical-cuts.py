class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        MOD = 10**9+7
        
        hc = [0] + hc + [h]
        vc = [0] + vc + [w]
        
        hc.sort()
        vc.sort()
        
        maxh, maxw = 0, 0
        
        for i in range(1, len(vc)):
            maxw = max(maxw, vc[i] - vc[i-1])
            
        for i in range(1, len(hc)):
            maxh = max(maxh, hc[i] - hc[i-1])
            
        return (maxw * maxh) % MOD