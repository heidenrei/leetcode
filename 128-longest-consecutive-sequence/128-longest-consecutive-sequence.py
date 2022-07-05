class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        
        mini = min(nums)
        maxi = max(nums)
        
        rising_best = 0
        falling_best = 0
        
        curr = 0
        
        for x in range(mini, mini+10**5+1):
            if x in nums:
                curr += 1
                if curr > rising_best:
                    rising_best = curr
            else:
                curr = 0
        
        curr = 0
        for x in range(maxi, maxi-10**5-1):
            if x in nums:
                curr += 1
                if curr > falling_best:
                    falling_best = curr
            else:
                curr = 0
                
        return max(rising_best, falling_best)