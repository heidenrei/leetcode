class Solution:
    def maximumUnits(self, boxes: List[List[int]], k: int) -> int:
        boxes.sort(key=lambda x: (-x[1], x[0]))
        i = 0
        ans = 0
        
        while k > 0 and i < len(boxes):
            if boxes[i][0] <= k:
                ans += boxes[i][0] * boxes[i][1]
                k -= boxes[i][0]
                i += 1
            else:
                ans += k * boxes[i][1]
                break
                
        return ans