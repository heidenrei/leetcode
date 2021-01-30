class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ans = [area, 1]
        
        for x in range(2, math.ceil(math.sqrt(area)+1)):
            if area % x == 0:
                ans = [area//x, x]
                
        return sorted(ans)[::-1]