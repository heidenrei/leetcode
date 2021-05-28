class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums) + 2
        nums = [1] + nums + [1]
        
        @cache
        def go(l, r):
            if l == r:
                return nums[l]
            
            best = 0
            
            for m in range(l+1, r):
                tmp = nums[l]*nums[m]*nums[r] + go(l, m) + go(m, r)
                
                if tmp > best:
                    best = tmp
                
            return best
        
        return go(0, N-1)