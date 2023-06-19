class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        curr = 0
        for d in gain:
            curr += d
            ans = max(ans, curr)
        return ans