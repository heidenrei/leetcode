class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        boxTypes = deque(boxTypes)
        
        ans = 0
                
        while truckSize and boxTypes:
            x, y = boxTypes.popleft()
            while x and truckSize:
                x -= 1
                ans += y
                truckSize -= 1
        return ans
