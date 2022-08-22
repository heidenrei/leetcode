class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        N = len(nums)

        # keep a decreasing mq while iterating from right
        mq = [[-inf, N]]
        ans = 0
        for i in range(N-1, -1, -1):
            while nums[i] <= mq[-1][0]:
                mq.pop()
            ans += mq[-1][1] - i
            mq.append([nums[i], i])
        return ans