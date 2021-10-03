class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q = [0]
        best = 0
        N = len(nums)
        for i in range(N):
            if i <= best:
                best = max(best, nums[i] + i)
                if best >= N - 1:
                    return True
            else:
                return False