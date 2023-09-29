class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        runs = []
        run = 1
        ans = 0
        curr = nums[0]
        for x in nums[1:]:
            if x > curr:
                run += 1
                curr = x
            else:
                ans += (run*(run+1))//2
                run = 1
                curr = x
        ans += (run*(run+1))//2
        return ans