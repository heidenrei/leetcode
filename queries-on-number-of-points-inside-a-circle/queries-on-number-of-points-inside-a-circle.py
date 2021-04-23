class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # get euc dist from each query and see if dist to point is <= r
        ans = []
        for x1, y1, r in queries:
            tmp = 0
            for x2, y2 in points:
                if math.sqrt((x1-x2)**2 + (y1-y2)**2) <= r:
                    tmp += 1
                    
            ans.append(tmp)
            
        return ans