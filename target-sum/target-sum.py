import copy

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:        
        N = len(nums)
        @cache
        def go(idx, curr):
            if idx == N:
                if curr == target:
                    return 1
                else:
                    return 0
            
            
            ans = 0
            ans += go(idx+1, curr+nums[idx])
            ans += go(idx+1, curr-nums[idx])
            
            return ans
        
        return go(0, 0)
            
            
        