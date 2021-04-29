class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window that always contains <= k 0s
        N = len(nums)
        best = 0
        j = 0
        for i in range(N):
            if nums[i] == 0:
                k -= 1
                if k < 0:
                    while nums[j] != 0:
                        j += 1
                    if nums[j] == 0:
                        k += 1
                        j += 1
            best = max(best, i - j + 1)
            
        return best