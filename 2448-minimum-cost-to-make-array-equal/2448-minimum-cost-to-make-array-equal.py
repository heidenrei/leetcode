class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        N = len(nums)
        nums = list(zip(nums, cost))
        nums.sort()
        sumi = sum(cost)
        k = sumi/2
        curr = 0
        if N & 1:
            for i in range(N):
                curr += nums[i][1]
                if curr >= k:
                    target = nums[i][0]
                    break
            ans = 0
            for x,y in nums:
                d = abs(x-target)
                ans += d*y
            return ans
        else:
            curr = 0
            for i in range(N):
                curr += nums[i][1]
                if curr >= k:
                    left = nums[i][0]
                    break
            curr = 0
            for i in range(N-1, -1, -1):
                curr += nums[i][1]
                if curr >= k:
                    right = nums[i][0]
                    break
                    
            left_ans = 0
            for x,y in nums:
                d = abs(x-left)
                left_ans += d*y
            right_ans = 0
            for x,y in nums:
                d = abs(x-right)
                right_ans += d*y
            return min(left_ans, right_ans)