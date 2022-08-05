class Solution:
    def combinationSum4(self, nums: List[int], T: int) -> int:
        N = len(nums)
        @lru_cache(None)
        def go(rem):
            if rem == 0:
                return 1
            
            ways = 0
            for num in nums:
                if rem-num >= 0:
                    ways += go(rem-num)
                
            return ways
        return go(T)