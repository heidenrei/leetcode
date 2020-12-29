class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # N^2*log(N) one-liner
        return [list(sorted(nums)).index(x) for x in nums]
