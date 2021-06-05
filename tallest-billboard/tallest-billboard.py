class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        N = len(rods)
        
        @cache
        def go(idx, diff):
            if idx == N:
                return 0 if diff == 0 else -math.inf
            
            addir = go(idx+1, diff+rods[idx]) + rods[idx]
            addil = go(idx+1, diff-rods[idx]) + rods[idx]
            skipi = go(idx+1, diff)
            
            return max([addir, addil, skipi])
            
        return go(0, 0) // 2