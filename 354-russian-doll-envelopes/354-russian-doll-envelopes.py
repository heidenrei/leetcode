class Solution:
    def maxEnvelopes(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for x,y in nums:
            idx = bisect_left(dp, y)
            if idx == len(dp):
                dp.append(y)
            else:
                dp[idx] = y
        return len(dp)