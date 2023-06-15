class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        N = len(nums)
        ans = []
        lower -= 1
        for x in nums:
            if x - 1 > lower:
                ans.append([lower+1, x-1])
            lower = x
        if lower < upper:
            ans.append([lower+1, upper])
        return ans