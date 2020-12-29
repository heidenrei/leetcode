class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        d = defaultdict(int)
        
        for i in range(N):
            if nums[i] in d:
                return [d[nums[i]], i]
            d[target-nums[i]] = i
            
