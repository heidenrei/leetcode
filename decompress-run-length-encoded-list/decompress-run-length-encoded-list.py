class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []
        for i in range(0, N-1, 2):
            coef, val = nums[i:i+2]
            for i in range(coef):
                ans.append(val)
        return ans
