class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        mq = []
        ans = [-inf]*N
        for i in range(N-1, -1, -1):

            while mq and mq[-1] <= nums[i]:
                mq.pop()
            if mq and nums[i] < mq[-1]:
                ans[i] = mq[-1]
            mq.append(nums[i])
        
        mq = []
        for i in range(N):
            if ans[i] == -inf:
                idx = bisect_right(mq, nums[i])
                if idx < len(mq):
                    ans[i] = mq[idx]
            if mq and nums[i] > mq[-1]:
                mq.append(nums[i])
            if not mq:
                mq.append(nums[i])
        
        for i in range(N):
            if ans[i] == -inf:
                ans[i] = -1
                
        return ans