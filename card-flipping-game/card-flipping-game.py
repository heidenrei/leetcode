class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        N = len(fronts)
        
        nums = sorted(list(set(fronts + backs)))
        
        def is_good(x):
            x = nums[x]
            for i in range(N):
                if (fronts[i] == x) & (backs[i] == x):
                    return False
            return True
                
        for x in range(len(nums)):
            if is_good(x):
                return nums[x]
            
        return 0