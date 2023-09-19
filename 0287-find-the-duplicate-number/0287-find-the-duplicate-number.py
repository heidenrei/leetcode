class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while nums[i] > 0:
            tmp=nums[i]
            nums[i] = 0
            i = tmp
        return i