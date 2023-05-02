class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            N = len(nums)
            cnt = 0
            new = []
            for i in range(0, N, 2):
                if cnt & 1:
                    new.append(max(nums[i], nums[i+1]))
                else:
                    new.append(min(nums[i], nums[i+1]))
                cnt += 1
            nums = new
        return nums[0]