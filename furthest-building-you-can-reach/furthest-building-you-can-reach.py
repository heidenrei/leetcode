class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def is_possible(idx):
            tmp_heights = heights[:idx+1]
            gaps = []
            for i in range(1, len(tmp_heights)):
                if tmp_heights[i] > tmp_heights[i-1]:
                    gaps.append(tmp_heights[i]-tmp_heights[i-1])
            gaps.sort(reverse=True)
            tmp_bricks = bricks
            tmp_idx = ladders
            if sum(gaps[tmp_idx:]) <= bricks:
                return True
            return False
        
        l = 0
        r = len(heights)
        
        while l < r:
            m =  (l+r)>>1
            if is_possible(m):
                l = m + 1
            else:
                r = m
                
        return l - 1