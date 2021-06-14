class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        N = len(nums)
        
        @cache
        def go(k):
            if nums[k] != k and nums[k] not in seen:
                seen.add(nums[k])
                return go(nums[k]) + 1
            else:
                return 0
        
        best = 1
        for x in range(N):
            seen = set([x])
            best = max(best, go(x)+1)
            
        return best