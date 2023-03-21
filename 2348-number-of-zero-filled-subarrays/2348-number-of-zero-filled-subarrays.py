class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        for k, v in groupby(nums, key=lambda x: not x):
            if k:
                v = len(list(v))
                ans += (v*(v+1))//2
                
        return ans