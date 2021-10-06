class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []
        for _ in range(5):
            for i in range(N):
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            
        for i in range(N):
            if nums[i] != i+1:
                ans.append(nums[i])
                
        return ans