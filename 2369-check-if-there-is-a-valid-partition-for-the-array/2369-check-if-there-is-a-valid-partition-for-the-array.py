class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        @cache
        def go(i):
            if i == N:
                return True
            if i + 2 < N:
                if ((nums[i] == nums[i+1] == nums[i+2]) or (nums[i] == nums[i+1]-1 == nums[i+2]-2)) and go(i+3):
                    return True
            if i + 1 < N and nums[i] == nums[i+1] and go(i+2):
                return True
            return False
        
        return go(0)