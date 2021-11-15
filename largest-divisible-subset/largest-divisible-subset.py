class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        nums.sort()
        dp = [set() for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0 :
                    if 1 + len(dp[j]) > len(dp[i]) :
                        dp[i] = dp[j] | {nums[i]}
            dp[i] |= {nums[i]}
        return max(dp, key = len)