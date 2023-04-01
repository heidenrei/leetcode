

class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        h = []
        s = 0
        ans = 0
        for x in nums:
            s += x
            heappush(h, x)
            while s < 0:
                s -= heappop(h)
                ans += 1

        return ans