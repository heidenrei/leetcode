from functools import reduce

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        
        is_calc = [[False] * 2 for _ in range(N)]
        calc_res = [[0] * 2 for _ in range(N)]
        
        @functools.lru_cache(None)
        def go(idx, cnt):
            if N == idx:
                return 1
            
            if nums[idx] == 0:
                return 0
            
            best = nums[idx]
            
            input_cnt_neg = cnt
            
            if nums[idx] < 0:
                cnt += 1
                cnt %= 2
            if input_cnt_neg == 0:
                best = max(best, nums[idx] * go(idx+1, cnt))
            else:
                best = min(best, nums[idx] * go(idx+1, cnt))
            
            return best
        
        best = float('-inf')
        
        for idx in range(N):
            best = max(best, go(idx, 0))
        return best