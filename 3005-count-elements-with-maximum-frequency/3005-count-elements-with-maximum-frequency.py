class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxi = max(c.values())
        ans = 0
        for v in c.values():
            if v == maxi:
                ans += 1
                
        return ans*maxi