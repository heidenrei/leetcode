class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        nums = sorted([a, b, c])
        if nums[1] - nums[0] == 1 and nums[2] - nums[1] == 1:
            low = 0
        elif nums[1] - nums[0] <= 2 or nums[2] - nums[1] <= 2:
            low = 1
        else:
            low = 2            
        
        return [low, (nums[2]-nums[1]-1)+(nums[1]-nums[0]-1)]