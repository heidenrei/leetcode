class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        N = len(nums)
        maxi = max(nums)
        s = set(nums)
        ans = 0
        for g in range(1, maxi+1):
            rungcd = 0
            for x in range(g, 2*10**5+1, g):
                if x in s:
                    rungcd = gcd(rungcd, x)
                    if rungcd == g:
                        break
            ans += rungcd == g
            
        return ans