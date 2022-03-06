class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)
        nums = list(set(nums))
        nums.sort(reverse=True)
        N = len(nums)

        @cache
        def go(i): # at i we haven't picked i yet
            if i >= N:
                return 0
            if i + 1 < N and nums[i+1] == nums[i] - 1:
                return max(go(i+1), go(i+2) + c[nums[i]] * nums[i])
            else:
                return go(i+1) + c[nums[i]] * nums[i]
        return go(0)