class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        
        if target % 1 != 0 or max(nums) > target:
            return False
        
        N = len(nums)
        
        @lru_cache(None)
        def go(idx, remainder):
            if idx == N:
                return False
            if remainder == 0:
                return True
            
            return go(idx+1, remainder-nums[idx]) or go(idx+1, remainder)
        
        return go(0, target)