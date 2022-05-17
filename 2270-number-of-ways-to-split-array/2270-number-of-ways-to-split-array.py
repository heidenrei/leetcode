from sortedcontainers import SortedList

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        N = len(nums)
        sl = SortedList(nums)
        rsum = sum(nums)
        lsum = 0
        ans = 0
        for i in range(N-1):
            lsum += nums[i]
            rsum -= nums[i]
            ans += lsum >= rsum
                
        return ans