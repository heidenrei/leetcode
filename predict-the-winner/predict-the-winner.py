class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        
        @cache
        def go(i, j):
            if i > j:
                return 0
            p1_turn = (N - j + i) & 1
            if p1_turn:
                return max(go(i+1, j) + nums[i], go(i, j-1) + nums[j])
            else:
                return min(go(i+1, j) - nums[i], go(i, j-1) - nums[j])
        
        return go(0, N-1) >= 0
                
            