class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int)
        pfs = 0
        ans = 0
        for x in nums:
            pfs += x
            ans += d[pfs-goal]
            d[pfs] += 1
            
        return ans + d[goal]