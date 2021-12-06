class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = 0
        evens = 0
        
        for i in range(len(position)):
            if position[i] & 1:
                odds += 1
            else:
                evens += 1
                
        return min(odds, evens)